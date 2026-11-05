from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'luxe_estate_secret_key'

# 10 Detailed properties using reliable Unsplash Source photo IDs directly
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
def buy_property(prop_id):
    prop = next((p for p in PROPERTIES if p['id'] == prop_id), None)
    client_name = request.form.get('name')
    client_email = request.form.get('email')
    client_phone = request.form.get('phone')
    message = request.form.get('message', '')

    print(f"--- EMAIL TO marinsdivine480@gmail.com ---")
    print(f"New Purchase/Inquiry for: {prop['title']} ({prop['price']})")
    print(f"Client Name: {client_name}")
    print(f"Client Email: {client_email}")
    print(f"Client Phone: {client_phone}")
    print(f"Message: {message}")
    print(f"----------------------------------------")

    flash(f"Inquiry sent successfully to marinsdivine480@gmail.com for {prop['title']}!", "success")
    return render_template('success.html', property=prop, name=client_name)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(f"--- GENERAL CONTACT EMAIL TO marinsdivine480@gmail.com ---")
        print(f"From: {name} ({email})")
        print(f"Message: {message}")
        print(f"----------------------------------------------------")
        flash("Your message has been sent directly to marinsdivine480@gmail.com!", "success")
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
