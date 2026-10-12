# Static page builder for the Bleuvets concept (Dunlap ranch, Austin). Run: python3 build.py
from lib import CFG, img, page, bc, finish
BASE='https://bleuvets-demo.vercel.app/'
TEL,TEL_H='+15125223018','(512) 522&#8209;3018'
MAIL='bleuvetsrentals@gmail.com'
AIRBNB='https://www.airbnb.com/rooms/1171734395727141363'
HF='https://bleuvets.holidayfuture.com/listings/278348'
STUB='<svg class="stub" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18v4a2 2 0 0 0 0 4v4H3v-4a2 2 0 0 0 0-4z"/><path d="M9 6v12" stroke-dasharray="2 2"/></svg>'
ORG={"@context":"https://schema.org","@type":"VacationRental","name":"Bleuvets Dunlap Ranch","alternateName":"Theatre, 3 Acre LUXE Ranch, Near COTA","url":BASE,
 "description":"Private 3 acre ranch in Del Valle, east Austin, with 5 bedrooms, 9 beds, 3 bathrooms, 2 kitchens and a home theater. Sleeps 14.",
 "telephone":"+1-512-522-3018","email":MAIL,"brand":{"@type":"Brand","name":"Bleuvets"},
 "address":{"@type":"PostalAddress","addressLocality":"Del Valle","addressRegion":"TX","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":30.247,"longitude":-97.562},
 "containsPlace":{"@type":"Accommodation","numberOfBedrooms":5,"numberOfBathroomsTotal":3,"occupancy":{"@type":"QuantitativeValue","maxValue":14},"bed":"1 king, 3 queen, 1 full, 4 twin"},
 "aggregateRating":{"@type":"AggregateRating","ratingValue":4.93,"reviewCount":42,"bestRating":5},
 "checkinTime":"16:00","checkoutTime":"10:00","petsAllowed":True,"image":BASE+"img/deck-string-lights.webp","sameAs":[AIRBNB,HF]}
CFG.update(base=BASE,name='Bleuvets',theme='#14213d',org=ORG,
 fonthead='<link rel="preload" as="font" type="font/woff2" href="fonts/fraunces-normal-700-latin.woff2" crossorigin><link rel="preload" as="font" type="font/woff2" href="fonts/figtree-normal-400-latin.woff2" crossorigin>',
 icon="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%2314213d'/%3E%3Ctext x='16' y='23' font-family='Georgia' font-size='20' font-weight='700' text-anchor='middle' fill='%23c9a24a'%3EB%3C/text%3E%3C/svg%3E",
 bar='Not the official Bleuvets site. Photos and details come from the public Airbnb listing for this home and are used for this pitch only.',
 nav=[('the-house.html','The house'),('theater.html','Theater'),('the-stay.html','Plan your stay'),('book.html','Book')],
 mark='<a class="mark" href="index.html" aria-label="Bleuvets home"><span class="b-badge" aria-hidden="true">B</span><span class="b-name"><b>Bleuvets</b><small>Dunlap Ranch &middot; Austin</small></span></a>',
 cta='<a class="btn" href="book.html">Check dates</a>',
 foot=f'''<footer class="foot"><div class="wrap">
<div class="foot-spread"><div><p class="kicker" style="color:var(--brass)">{STUB} Your group, fourteen seats</p><p class="foot-big">Book the whole ranch.<br><a href="tel:{TEL}">{TEL_H}</a></p><p><a href="mailto:{MAIL}">{MAIL}</a></p></div>
<div class="foot-cols"><div><h2>The ranch</h2><ul><li><a href="the-house.html">Rooms and beds</a></li><li><a href="theater.html">The theater room</a></li><li><a href="the-house.html#outside">Three acres outside</a></li></ul></div>
<div><h2>Your stay</h2><ul><li><a href="the-stay.html#getting-here">Getting here</a></li><li><a href="the-stay.html#rules">House rules</a></li><li><a href="the-stay.html#faq">Questions</a></li><li><a href="book.html">Check dates</a></li></ul></div>
<div><h2>Also on</h2><ul><li><a href="{AIRBNB}" rel="noopener">Airbnb</a></li><li><a href="{HF}" rel="noopener">Bleuvets direct portal</a></li></ul></div></div></div>
<div class="foot-row"><span>Bleuvets &middot; Del Valle, east Austin, Texas</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>''')

FACTS=[('14','guests'),('5','bedrooms'),('9','beds'),('3','full baths'),('2','kitchens'),('3','acres')]
def factrow(): return '<ul class="ticket-facts">'+''.join(f'<li><b>{n}</b><span>{l}</span></li>' for n,l in FACTS)+'</ul>'
CATS=[('Check in','4.98'),('Communication','4.98'),('Accuracy','4.95'),('Value','4.93'),('Cleanliness','4.9'),('Location','4.88')]

# ---------- HOME ----------
page('index.html','Austin Ranch Rental Near COTA, Sleeps 14 | Bleuvets Dunlap',
 'A private 3 acre ranch in east Austin with a home theater, two kitchens and room for 14. Rated 4.93 from 42 Airbnb stays. Check your dates with Bleuvets today.', f'''
<section class="hero"><div class="hero-photo">{img('deck-string-lights.webp','The ranch deck under string lights at dusk, with the lawn and oak trees behind it',eager=True,sizes='100vw')}</div>
<div class="wrap hero-inner"><div class="ticket rv">
 <p class="kicker">{STUB} Del Valle &middot; east Austin, Texas</p>
 <h1>Three acres, a home theater and room for <em>fourteen.</em></h1>
 <p class="lede">The Bleuvets Dunlap ranch is two renovated homes on one private lot, booked by one group at a time. The host puts it about 10 minutes from the airport and Circuit of the Americas.</p>
 {factrow()}
 <div class="cta"><a class="btn" href="book.html">Check your dates</a><a class="btn btn--plain" href="the-house.html">Walk through the house</a></div>
</div>
<a class="score rv" href="{AIRBNB}" rel="noopener"><span class="score-n">4.93</span><span class="score-t"><b>42 reviews on Airbnb</b><small>Superhost &middot; Guest favorite</small></span></a>
</div></section>

<section class="marquee-strip" aria-label="What the ranch is built for"><div class="wrap ms-grid">
 <p class="ms-item rv"><b>F1 and race weekends</b><span>Circuit of the Americas is the closest big venue.</span></p>
 <p class="ms-item rv"><b>Family reunions</b><span>Two kitchens, one huge table, bunk room for the kids.</span></p>
 <p class="ms-item rv"><b>Work trips and long stays</b><span>Close to Tesla Giga Texas, with Starlink WiFi and a washer and dryer.</span></p>
</div></section>

<section class="now-showing"><div class="wrap ns-grid">
 <figure class="ns-photo rv">{img('theater.webp','The home theater room with red curtains, sectionals and a big screen',sizes='(max-width:900px) 100vw, 60vw')}</figure>
 <div class="ns-copy rv"><p class="kicker">{STUB} Now showing</p><h2>A real movie room, with bunk beds in the back row.</h2>
 <p>Red curtains, a big screen, deep sectionals and a disco ball. The listing calls it the cinematic media room. Bedroom 5 lives in here too, with four twins and a full in bunk beds, so the kids can fall asleep to the credits.</p>
 <a class="btn btn--plain" href="theater.html">See the theater</a></div>
</div></section>

<section class="spaces"><div class="wrap">
 <div class="sp-head rv"><p class="kicker">{STUB} Inside</p><h2>Two homes on one lot, booked together.</h2><p>Your reservation includes both fully renovated living units. Everyone is on the same property, and each group still has a door to close.</p></div>
 <div class="sp-mosaic">
  <figure class="m1 rv">{img('kitchen-island.webp','Bright kitchen with a long island and bar stools',sizes='(max-width:900px) 100vw, 50vw')}<figcaption>Kitchen one, island seating</figcaption></figure>
  <figure class="m2 rv">{img('living-library.webp','Living room with tall shelving and a library ladder',sizes='(max-width:900px) 100vw, 30vw')}<figcaption>Living room and loft shelving</figcaption></figure>
  <figure class="m3 rv">{img('kitchen-two.webp','Second kitchen with open shelving and a range hood',sizes='(max-width:900px) 100vw, 30vw')}<figcaption>Kitchen two</figcaption></figure>
  <figure class="m4 rv">{img('bedroom-king.webp','King bedroom with white linens',sizes='(max-width:900px) 100vw, 30vw')}<figcaption>Bedroom 1, king</figcaption></figure>
 </div>
 <a class="btn" href="the-house.html">Every room, bed by bed</a>
</div></section>

<section class="outside"><div class="outside-photo">{img('ranch-lawn.webp','The wide lawn and oak trees in front of the ranch house',sizes='100vw')}</div>
<div class="wrap"><div class="outside-card rv"><p class="kicker" style="color:var(--brass)">{STUB} Outside</p><h2>Room for the kids to run.</h2><p>About three acres with a swing, a climbing rope, a BBQ area, a fire pit and outdoor games. String lights over the deck for the evenings.</p></div></div></section>

<section class="ratings"><div class="wrap rt-grid">
 <div class="rv"><p class="kicker">{STUB} From 42 stays on Airbnb</p><h2>4.93 overall. Check in and communication score highest.</h2>
 <p class="note">Category scores from the public Airbnb listing as of 12 October 2026. We left guest reviews off this concept until Bleuvets picks the ones to feature.</p></div>
 <ul class="cats rv">{''.join(f'<li><span>{a}</span><b>{b}</b><i style="--w:{float(b)/5*100:.1f}%"></i></li>' for a,b in CATS)}</ul>
 <div class="ph rv"><b>Placeholder</b>A live strip of three Airbnb reviews, chosen by Bleuvets and linked to the originals, goes here.</div>
</div></section>

<section class="direct"><div class="wrap dir-grid rv">
 <div><p class="kicker" style="color:var(--brass)">{STUB} Book direct</p><h2>Talk to the host before you book.</h2><p>Large group, pets, an event or a long stay? Call or email Bleuvets first and get a straight answer on the rules and the rate.</p></div>
 <div class="dir-cta"><a class="btn" href="book.html">Check dates</a><a class="btn btn--plain dark" href="tel:{TEL}">Call {TEL_H}</a></div>
</div></section>''', extra_ld=[bc(('Home',''))])

# ---------- THE HOUSE ----------
BEDS=[('Bedroom 1','1 king bed','bedroom-king.webp','King bedroom with white linens and a window'),
 ('Bedroom 2','1 queen bed','bedroom-queen.webp','Queen bedroom with a wooden headboard'),
 ('Bedroom 3','1 queen bed',None,None),('Bedroom 4','1 queen bed',None,None),
 ('Bedroom 5','4 twin beds and 1 full, in bunks','theater-bunks.webp','Bunk beds at the back of the theater room')]
page('the-house.html','Rooms, Beds and Kitchens at the Dunlap Ranch | Bleuvets',
 'Five bedrooms, nine beds, three full baths and two full kitchens across two renovated homes on one private Austin lot. See every room, then check your dates.', f'''
<section class="page-head"><div class="wrap ph-grid"><div class="rv"><p class="kicker">{STUB} The house</p><h1>Five bedrooms, nine beds, two kitchens.</h1>
<p class="lede">Two fully renovated living units on one private three acre lot. The whole property is yours; it is never shared with another booking.</p></div>{factrow()}</div></section>
<section class="beds"><div class="wrap"><h2 class="rv">Who sleeps where</h2><div class="bed-list">
{''.join(f'<article class="bed rv">'+(img(i,a,sizes='(max-width:700px) 100vw, 33vw') if i else '<div class="bed-ph">Photo coming from Bleuvets</div>')+f'<div class="bed-t">{STUB}<h3>{n}</h3><p>{b}</p></div></article>' for n,b,i,a in BEDS)}
</div><p class="note rv">Bedroom 5 also has two large sectionals. The listing does not count them as beds. Fresh linens, pillows and blankets come with every advertised bed.</p></div></section>
<section class="kitchens"><div class="wrap k-grid">
<figure class="rv">{img('kitchen-island.webp','Kitchen with a long island and seating',sizes='(max-width:900px) 100vw, 55vw')}</figure>
<div class="rv"><p class="kicker">{STUB} Kitchens and dining</p><h2>Cook for three families at once.</h2><p>Two well equipped kitchens with pots and pans, utensils, plates, bowls, glasses, mugs and standard appliances. Eat at the large dining table, the island or the breakfast nook.</p>
<figure class="k-small">{img('dining.webp','Dining table for a big group',sizes='(max-width:900px) 100vw, 30vw')}</figure></div></div></section>
<section class="baths"><div class="wrap b-grid"><div class="rv"><p class="kicker">{STUB} Three full baths</p><h2>Towels and the basics are on us.</h2><p>Fresh towels, shampoo, body wash, hand soap, hair dryers and essential toiletries in all three bathrooms.</p></div><figure class="rv">{img('bath.webp','Full bathroom with a double vanity',sizes='(max-width:900px) 100vw, 40vw')}</figure></div></section>
<section class="outside-list" id="outside"><div class="wrap ol-grid">
<figure class="rv">{img('ranch-oaks.webp','Oak trees and open lawn on the ranch',sizes='(max-width:900px) 100vw, 50vw')}</figure>
<div class="rv"><p class="kicker">{STUB} Outside and extras</p><h2>Three acres and a list of things to do.</h2>
<ul class="ticks"><li>Private home theater</li><li>Arcade, karaoke and board games</li><li>BBQ area and fire pit</li><li>Swing, climbing rope and outdoor games</li><li>Smart TVs (bring your own streaming logins)</li><li>Starlink WiFi, central air and heat</li><li>Washer, dryer, iron and ironing board</li><li>A foldable baby playard</li><li>Free parking in the garage and driveway</li></ul></div></div></section>
''', extra_ld=[bc(('Home',''),('The house','the-house.html'))])

# ---------- THEATER ----------
page('theater.html','The Home Theater Room at the Dunlap Ranch | Bleuvets Austin',
 'Red curtains, a big screen, deep sectionals and bunk beds for the kids. See the home theater room at the Bleuvets ranch near COTA, then check your dates.', f'''
<section class="theater-hero"><div class="th-photo">{img('theater-screen.webp','The theater room with its big projection screen and sectional seating',eager=True,sizes='100vw')}</div>
<div class="wrap th-copy rv"><p class="kicker" style="color:var(--brass)">{STUB} Now showing</p><h1>The movie room your group will talk about.</h1><p class="lede">Big screen, red curtains, deep sectionals and a disco ball, plus arcade, karaoke and board games so nobody is bored on site.</p></div></section>
<section class="th-strip"><div class="wrap th-grid">
<figure class="rv">{img('theater.webp','Theater room with red curtains and a skylight',sizes='(max-width:900px) 100vw, 50vw')}<figcaption>Seats for everyone</figcaption></figure>
<figure class="rv">{img('theater-bunks.webp','Bunk beds in the theater room',sizes='(max-width:900px) 100vw, 50vw')}<figcaption>Bedroom 5 sleeps five in bunks</figcaption></figure>
</div><p class="note wrap">Streaming subscriptions are not provided. Sign in with your own accounts on the smart TVs.</p></section>
''', extra_ld=[bc(('Home',''),('Theater','theater.html'))])

# ---------- THE STAY ----------
FAQ=[('How many people can stay?','Up to 14 overnight guests. The nightly rate covers 6, and each extra guest from number 7 is $55 a night. Every overnight guest and visitor has to be disclosed in advance.'),
 ('Are pets allowed?','House trained pets are welcome with approval. The fee is $150 per pet, per stay. Pets stay off the beds and furniture, and waste gets picked up.'),
 ('Can we host an event or a shoot?','Only with written approval first. Events, gatherings, commercial photography and filming may carry extra fees, parking rules and a separate agreement. Unapproved parties are not allowed.'),
 ('Where do we park?','In the garage or the driveway. Street parking is not allowed. Tell Bleuvets before you book if you are bringing several cars.'),
 ('What are check in and check out times?','Check in is 4 pm and check out is 10 am on the Bleuvets booking portal. Early check in and late check out depend on availability and need approval.'),
 ('Are there cameras?','Seven exterior cameras record the deck, entrance walkway, rear fence, backyard, barn fence, driveway and front yard. There are none inside. A noise monitor measures decibel levels only and records no audio.'),
 ('How is the internet?','Starlink satellite is the only service out here. It handles normal browsing and streaming, though weather can affect it.'),
 ('Can we smoke?','Not indoors, including vaping. Outdoors is fine if butts are disposed of properly.')]
page('the-stay.html','Plan Your Stay: Rules, Parking and FAQ | Bleuvets Ranch Austin',
 'House rules, pets, parking, cameras and check in times for the Bleuvets ranch in Del Valle, east Austin. Read the answers here, then call or check your dates.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{STUB} Plan your stay</p><h1 class="rv">Straight answers before you book.</h1><p class="lede rv">Everything here comes from the house rules Bleuvets publishes on its listing.</p></div></section>
<section class="getting" id="getting-here"><div class="wrap gh-grid"><div class="rv"><h2>Getting here</h2><p>The ranch is in Del Valle on the east side of Austin. The host lists it about 10 minutes from Austin Bergstrom airport and Circuit of the Americas, close to Tesla Giga Texas, and roughly 15 to 20 minutes from downtown.</p>
<div class="ph"><b>Placeholder</b>Exact drive times from the address, plus a map, once Bleuvets confirms what it wants public. The address is shared after booking.</div></div>
<ul class="dist rv"><li><b>~10 min</b><span>Austin airport</span></li><li><b>~10 min</b><span>Circuit of the Americas</span></li><li><b>Minutes</b><span>Tesla Giga Texas</span></li><li><b>15 to 20 min</b><span>Downtown Austin</span></li></ul></div></section>
<section class="rules" id="rules"><div class="wrap"><h2 class="rv">House rules, in short</h2><ol class="rule-list">{''.join(f'<li class="rv">{STUB}<span>{x}</span></li>' for x in ['One group at a time. The whole property is yours.','Up to 14 overnight guests, all disclosed in advance.','Pets with approval, $150 each per stay.','No unapproved parties or events.','Park in the garage or driveway only.','No smoking or vaping indoors.','Quiet hours, kept with a noise monitor that records no audio.'])}</ol></div></section>
<section class="faq" id="faq"><div class="wrap"><h2 class="rv">Questions</h2>{''.join(f'<details class="rv"><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)}</div></section>
''', extra_ld=[bc(('Home',''),('Plan your stay','the-stay.html')),{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}])

# ---------- BOOK ----------
page('book.html','Check Dates for the Dunlap Ranch in Austin | Bleuvets Direct',
 'Ask Bleuvets about dates, group size, pets or events at the 3 acre Dunlap ranch near COTA. Send an inquiry, call (512) 522 3018, or book on Airbnb today.', f'''
<section class="page-head"><div class="wrap"><p class="kicker rv">{STUB} Book</p><h1 class="rv">Tell us your dates and your crew.</h1></div></section>
<section class="book"><div class="wrap bk-grid">
<form class="bk-form rv" data-demo="Thanks. On the live site this goes straight to Bleuvets. (Demo: nothing was sent.)" novalidate>
<div class="two"><div class="fld"><label for="ci">Check in</label><input id="ci" name="ci" type="date" required></div><div class="fld"><label for="co">Check out</label><input id="co" name="co" type="date" required></div></div>
<div class="two"><div class="fld"><label for="g">Guests</label><select id="g" name="g">{''.join(f'<option>{i}</option>' for i in range(1,15))}</select></div><div class="fld"><label for="why">Trip</label><select id="why" name="why"><option>Family trip</option><option>Race weekend at COTA</option><option>Work or long stay</option><option>Event (needs approval)</option></select></div></div>
<div class="fld"><label for="nm">Name</label><input id="nm" name="nm" autocomplete="name" required></div>
<div class="two"><div class="fld"><label for="em">Email</label><input id="em" name="em" type="email" autocomplete="email" required></div><div class="fld"><label for="ph">Phone</label><input id="ph" name="ph" type="tel" autocomplete="tel"></div></div>
<div class="fld"><label for="msg">Anything we should know? Pets, cars, early arrival</label><textarea id="msg" name="msg"></textarea></div>
<button class="btn" type="submit">Send inquiry</button><p class="formmsg" role="status" aria-live="polite"></p></form>
<aside class="bk-side rv"><div class="ticket small"><p class="kicker">{STUB} Or book now</p><a class="btn" href="{AIRBNB}" rel="noopener">Book on Airbnb</a><a class="btn btn--plain" href="{HF}" rel="noopener">Bleuvets direct portal</a><p><a href="tel:{TEL}">{TEL_H}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p></div>
<div class="ph"><b>Placeholder</b>A live availability calendar and instant quote from the Bleuvets booking system goes here.</div>
<p class="note">Direct portal policy: full refund up to 14 days before arrival, half up to 7 days before.</p></aside>
</div></section>
''', extra_ld=[bc(('Home',''),('Book','book.html'))])

# ---------- 404 ----------
page('404.html','Page Not Found | Bleuvets Dunlap Ranch Concept, Austin TX',
 'That page is not part of the Bleuvets concept. Head back to the ranch home page, walk through the rooms, or check your dates for the Dunlap ranch in Austin.', f'''
<section class="page-head nf"><div class="wrap"><p class="kicker">{STUB} Wrong theater</p><h1>This screening was cancelled.</h1><p class="lede">The page you wanted is not here.</p><a class="btn" href="index.html">Back to the ranch</a></div></section>''')
finish(['index.html','the-house.html','theater.html','the-stay.html','book.html'])
print('built')
