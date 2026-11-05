from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sqlite3

app = Flask(__name__)
app.secret_key = 'luxe_estate_secure_super_secret_key_2026'

# Initialize CSRF Protection
csrf = CSRFProtect(app)

# Initialize Rate Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

def get_db_connection():
    conn = sqlite3.connect('real_estate.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_admin_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    # Check if Elder exists, if not create with hashed password
    cursor.execute("SELECT * FROM admin_users WHERE username = 'Elder'")
    if not cursor.fetchone():
        hashed_pw = generate_password_hash('Eyereforma')
        cursor.execute("INSERT INTO admin_users (username, password_hash) VALUES (?, ?)", ('Elder', hashed_pw))
        conn.commit()
    conn.close()

init_admin_user()

PROPERTIES = [
    {
        "id": 1,
        "title": "Modern Glass Villa",
        "location": "Beverly Hills, California",
        "price": "$2,450,000",
        "image_url": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=800&q=80",
        "description": "An architectural masterpiece featuring floor-to-ceiling glass walls, infinity pool, smart home automation, and panoramic views of the Beverly Hills canyon.",
        "beds": 5, "baths": 6, "sqft": 5400
    },
    {
        "id": 2,
        "title": "Contemporary Urban Penthouse",
        "location": "Manhattan, New York",
        "price": "$1,850,000",
        "image_url": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80",
        "description": "Luxurious penthouse in the heart of Manhattan with private elevator access, rooftop terrace, and breathtaking skyline views.",
        "beds": 3, "baths": 3, "sqft": 2800
    },
    {
        "id": 3,
        "title": "Serene Suburban Family Home",
        "location": "Austin, Texas",
        "price": "$920,000",
        "image_url": "https://images.unsplash.com/photo-1580587771525-78b9dba3b914?auto=format&fit=crop&w=800&q=80",
        "description": "Spacious family residence with lush green lawn, modern gourmet kitchen, covered patio, and top-tier school district proximity.",
        "beds": 4, "baths": 3, "sqft": 3600
    },
    {
        "id": 4,
        "title": "Minimalist Architectural Haven",
        "location": "Malibu, California",
        "price": "$3,100,000",
        "image_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80",
        "description": "Beachfront minimalist design offering direct ocean access, open-concept living spaces, and serene natural lighting throughout.",
        "beds": 4, "baths": 5, "sqft": 4200
    },
    {
        "id": 5,
        "title": "Lakeside Luxury Estate",
        "location": "Lake Tahoe, Nevada",
        "price": "$2,750,000",
        "image_url": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80",
        "description": "Mountain-meets-lake retreat featuring private boat dock, stone fireplace, vaulted timber ceilings, and heated wrap-around deck.",
        "beds": 6, "baths": 6, "sqft": 6100
    },
    {
        "id": 6,
        "title": "Classic Luxury Mansion",
        "location": "Greenwich, Connecticut",
        "price": "$3,890,000",
        "image_url": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=800&q=80",
        "description": "Gated historic estate set on 3 private acres featuring manicured gardens, tennis court, wine cellar, and grand ballroom.",
        "beds": 7, "baths": 8, "sqft": 8500
    },
    {
        "id": 7,
        "title": "Sunset Horizon Villa",
        "location": "Scottsdale, Arizona",
        "price": "$1,650,000",
        "image_url": "https://images.unsplash.com/photo-1600566753376-12c8ab7fb75b?auto=format&fit=crop&w=800&q=80",
        "description": "Desert oasis with resort-style backyard, custom fire pit, infinity pool facing the mountains, and luxury designer finishes.",
        "beds": 4, "baths": 4, "sqft": 3900
    },
    {
        "id": 8,
        "title": "Coastal Cliffside Retreat",
        "location": "Big Sur, California",
        "price": "$4,200,000",
        "image_url": "https://images.unsplash.com/photo-1600585154526-990dced4db0d?auto=format&fit=crop&w=800&q=80",
        "description": "Dramatic cliffside property overlooking the Pacific Ocean with unmatched privacy, organic architecture, and observatory deck.",
        "beds": 3, "baths": 4, "sqft": 3500
    },
    {
        "id": 9,
        "title": "Alpine Ski Chalet",
        "location": "Aspen, Colorado",
        "price": "$3,400,000",
        "image_url": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=800&q=80",
        "description": "Ski-in/ski-out luxury chalet with heated driveway, private hot tub, cedar sauna, and cozy rustic stone interiors.",
        "beds": 5, "baths": 6, "sqft": 4800
    },
    {
        "id": 10,
        "title": "Historic Brownstone Elegance",
        "location": "Boston, Massachusetts",
        "price": "$2,100,000",
        "image_url": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?auto=format&fit=crop&w=800&q=80",
        "description": "Meticulously restored historic brownstone blending original crown moldings with state-of-the-art kitchen and courtyard garden.",
        "beds": 4, "baths": 4, "sqft": 3200
    }
]

@app.route('/')
def home():
    return render_template('home.html', properties=PROPERTIES[:6])

@app.route('/listings')
def listings():
    return render_template('listings.html', properties=PROPERTIES)

@app.route('/property/<int:prop_id>')
def property_detail(prop_id):
    prop = next((p for p in PROPERTIES if p['id'] == prop_id), None)
    if not prop:
        return "Property not found", 404
    return render_template('property_detail.html', property=prop)

@app.route('/buy/<int:prop_id>', methods=['POST'])
@limiter.limit("10 per minute")
def buy_property(prop_id):
    prop = next((p for p in PROPERTIES if p['id'] == prop_id), None)
    client_name = request.form.get('name')
    client_email = request.form.get('email')
    client_phone = request.form.get('phone')
    message_text = request.form.get('message', '')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM conversations WHERE client_email = ? AND property_title = ? AND status = 'Open'",
        (client_email, prop['title'])
    )
    conv = cursor.fetchone()

    if conv:
        conv_id = conv['id']
    else:
        cursor.execute(
            "INSERT INTO conversations (client_name, client_email, client_phone, property_title, status) VALUES (?, ?, ?, ?, 'Open')",
            (client_name, client_email, client_phone, prop['title'])
        )
        conv_id = cursor.lastrowid

    cursor.execute(
        "INSERT INTO conversation_messages (conversation_id, sender, message) VALUES (?, 'client', ?)",
        (conv_id, message_text)
    )
    conn.commit()
    conn.close()

    session['client_email'] = client_email
    flash(f"Inquiry sent for {prop['title']}! You can track your conversation below.", "success")
    return redirect(url_for('customer_care', conv_id=conv_id))

@app.route('/customer-care', methods=['GET', 'POST'])
@limiter.limit("20 per minute", methods=['POST'])
def customer_care():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'new_conv':
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            property_title = request.form.get('property_title') or 'General Support'
            message_text = request.form.get('message')

            cursor.execute(
                "INSERT INTO conversations (client_name, client_email, client_phone, property_title, status) VALUES (?, ?, ?, ?, 'Open')",
                (name, email, phone, property_title)
            )
            conv_id = cursor.lastrowid
            cursor.execute(
                "INSERT INTO conversation_messages (conversation_id, sender, message) VALUES (?, 'client', ?)",
                (conv_id, message_text)
            )
            conn.commit()
            session['client_email'] = email
            conn.close()
            flash("New conversation started successfully!", "success")
            return redirect(url_for('customer_care', conv_id=conv_id))

        elif action == 'reply_conv':
            conv_id = request.form.get('conv_id')
            message_text = request.form.get('message')
            
            cursor.execute("SELECT status FROM conversations WHERE id = ?", (conv_id,))
            conv = cursor.fetchone()
            if conv and conv['status'] == 'Open':
                cursor.execute(
                    "INSERT INTO conversation_messages (conversation_id, sender, message) VALUES (?, 'client', ?)",
                    (conv_id, message_text)
                )
                conn.commit()
                flash("Reply sent successfully!", "success")
            else:
                flash("This conversation has been closed by customer care. Please start a new conversation.", "warning")
            conn.close()
            return redirect(url_for('customer_care', conv_id=conv_id))

    conv_id = request.args.get('conv_id', type=int)
    active_conv = None
    messages = []
    client_email = session.get('client_email')
    my_conversations = []

    if client_email:
        cursor.execute("SELECT * FROM conversations WHERE client_email = ? ORDER BY created_at DESC", (client_email,))
        my_conversations = cursor.fetchall()

    if conv_id:
        cursor.execute("SELECT * FROM conversations WHERE id = ?", (conv_id,))
        active_conv = cursor.fetchone()
        if active_conv:
            cursor.execute("SELECT * FROM conversation_messages WHERE conversation_id = ? ORDER BY created_at ASC", (conv_id,))
            messages = cursor.fetchall()
            session['client_email'] = active_conv['client_email']

    conn.close()
    return render_template('customer_care.html', 
                           active_conv=active_conv, 
                           messages=messages, 
                           my_conversations=my_conversations,
                           properties=PROPERTIES)

@app.route('/agent/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute", methods=['POST'])
def agent_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM admin_users WHERE username = ?", (username,))
        admin = cursor.fetchone()
        conn.close()

        if admin and check_password_hash(admin['password_hash'], password):
            session['agent_logged_in'] = True
            flash("Welcome back, Elder!", "success")
            return redirect(url_for('agent_dashboard'))
        else:
            flash("Invalid username or password.", "danger")
    return render_template('agent_login.html')

@app.route('/agent/dashboard')
def agent_dashboard():
    if not session.get('agent_logged_in'):
        return redirect(url_for('agent_login'))
    
    conn = get_db_connection()
    conversations = conn.execute('SELECT * FROM conversations ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('agent_dashboard.html', conversations=conversations)

@app.route('/agent/conversation/<int:conv_id>', methods=['GET', 'POST'])
def agent_conversation(conv_id):
    if not session.get('agent_logged_in'):
        return redirect(url_for('agent_login'))
    
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'reply':
            reply_text = request.form.get('message')
            cursor.execute(
                "INSERT INTO conversation_messages (conversation_id, sender, message) VALUES (?, 'agent', ?)",
                (conv_id, reply_text)
            )
            conn.commit()
            flash("Reply sent to client!", "success")
        elif action == 'close':
            cursor.execute("UPDATE conversations SET status = 'Closed' WHERE id = ?", (conv_id,))
            conn.commit()
            flash("Conversation closed successfully.", "success")

    cursor.execute("SELECT * FROM conversations WHERE id = ?", (conv_id,))
    conv = cursor.fetchone()
    cursor.execute("SELECT * FROM conversation_messages WHERE conversation_id = ? ORDER BY created_at ASC", (conv_id,))
    messages = cursor.fetchall()
    conn.close()

    return render_template('agent_conversation.html', conv=conv, messages=messages)

@app.route('/agent/logout')
def agent_logout():
    session.pop('agent_logged_in', None)
    flash("Logged out successfully.", "success")
    return redirect(url_for('agent_login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
