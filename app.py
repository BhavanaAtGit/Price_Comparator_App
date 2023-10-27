from flask import Flask, render_template, request
from utility import *

app  = Flask(__name__)

# route() decorator to tell Flask what URL should trigger our function
# The function is given a name which is also used to generate URLs for 
# that particular function, and returns the html page we want to display in the browser

prices_cache = {
    1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []
}

product_list = {
    1: {
        'title': 'APPLE iPhone 14 Pro',
        'image': 'static/images/iphone_14.jpg',
        'alt': 'iphone_14 pro image',
        'flipkart': 'https://www.flipkart.com/apple-iphone-14-pro-gold-128-gb/p/itme5895e593585d?pid=MOBGHWFHXPC3NFFY&lid=LSTMOBGHWFHXPC3NFFYC5Y9VU&marketplace=FLIPKART&q=iphone+14+pro&store=tyy%2F4io&srno=s_1_3&otracker=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_5_na_na_na&fm=Search&iid=569c34d1-a41f-44bc-ae9c-efb9f9e4bd58.MOBGHWFHXPC3NFFY.SEARCH&ppt=sp&ppn=sp&ssid=2aeymyx8pc0000001684948010657&qH=73a41d19c3188cc2',
        'reliance_digital': 'https://www.reliancedigital.in/apple-iphone-14-pro-128-gb-gold/p/493177780',
        'vijay_sales':'https://www.vijaysales.com/apple-iphone-14-pro-128-gb-gold/21975'
    },
    2: {
        'title': 'OPPO Enco Air 2 Pro',
        'image': 'static/images/oppo.jpg',
        'alt': 'OPPO Enco Air 2 Pro image',
        'flipkart':'https://www.flipkart.com/oppo-enco-air-2-pro-bluetooth-headset/p/itm01e94a1c117da?pid=ACCGCRT2GZZHQZ98&lid=LSTACCGCRT2GZZHQZ98IXM6U7&marketplace=FLIPKART&q=oppo+enco+air+2+pro&store=0pm%2Ffcn%2F821%2Fa7x%2F2si&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&fm=search-autosuggest&iid=952bfbbb-31e1-40ef-a0c3-dda028f701a8.ACCGCRT2GZZHQZ98.SEARCH&ppt=sp&ppn=sp&ssid=2mjb8hs09c0000001684936708897&qH=e333941bd7b33e61',
        'reliance_digital':'https://www.reliancedigital.in/oppo-enco-air-2-pro-wireless-earphone-with-active-noise-cancellation-white/p/492796951',
        'vijay_sales':'https://www.vijaysales.com/oppo-enco-air2-pro-truly-wireless-earbuds-with-active-noise-cancellation-28-hours-playback-with-the-charging-case-white/20823'
    },
    3: {
        'title': 'Acer aspire 5 core i5 Laptop',
        'image': 'static/images/laptop.jpg',
        'alt': 'acer aspire laptop image',
        'flipkart':'https://www.flipkart.com/acer-aspire-5-core-i5-11th-gen-8-gb-1-tb-hdd-256-gb-ssd-windows-10-home-a515-56-thin-light-laptop/p/itm07ce514e25a5d?pid=COMG69G2FNSS2MB2&lid=LSTCOMG69G2FNSS2MB2IKXJ6G&marketplace=FLIPKART&q=Acer+NX.A1GSI.00D+Aspire+5+Laptop&store=search.flipkart.com&srno=s_1_3&otracker=search&otracker1=search&fm=search-autosuggest&iid=655879ca-8e39-4e90-8884-7fb55e1a71f1.COMG69G2FNSS2MB2.SEARCH&ppt=sp&ppn=sp&ssid=04kk1h7va80000001684946214307&qH=e8fe689a57cbb5d8',
        'reliance_digital':'https://www.reliancedigital.in/acer-nx-a1gsi-00d-aspire-5-laptop-intel-core-i5-1135g7-8gb-512gb-ssd-intel-iris-xe-graphics-windows-11-mso-full-hd-39-6-cm-15-6-inch-/p/491998439',
        'vijay_sales':'https://www.vijaysales.com/acer-aspire-5-a515-56-51ev-nx-a1gsi-00d-laptop-11th-gen-core-i5-8gb-ram-512gb-ssd-15-6-39-6-cm-display-intel-iris-xe-graphics-win-11-mso/18761'
    },
    4: {
        'title': 'OnePlus Nord CE 2 Lite 5G',
        'image': 'static/images/oneplus.jpg',
        'alt': 'oneplus nord image',
        'flipkart':'https://www.flipkart.com/oneplus-nord-ce-2-lite-5g-blue-tide-128-gb/p/itm7acae55b999e6?pid=MOBGMFREBAHZQGY9&lid=LSTMOBGMFREBAHZQGY93P3KBS&marketplace=FLIPKART&q=OnePlus+Nord+CE+2+Lite+5G+%286+GB+RAM%2C+128+GB+ROM%2C+Blue+Tide%29&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=9727c1d7-795a-4432-8ede-a17cfe2d0536.MOBGMFREBAHZQGY9.SEARCH&ppt=sp&ppn=sp&ssid=9zf3i1um4w0000001685042093601&qH=b2ca5763f3237545',
        'reliance_digital':'https://www.reliancedigital.in/oneplus-nord-ce-2-lite-5g-128-gb-6-gb-ram-blue-tide-mobile-phone/p/492850035',
        'vijay_sales':'https://www.vijaysales.com/oneplus-nord-ce-2-lite-5g-6-gb-ram-128-gb-rom-blue-tide/20091'
    },
    5: {
        'title': 'SONY Smart TV',
        'image': 'static/images/sony.jpg',
        'alt': 'Sony TV image',
        'flipkart':'https://www.flipkart.com/sony-215-cm-85-inch-ultra-hd-4k-lcd-smart-android-tv/p/itm3e2ddf4ebd388?pid=TVSGJ6YFUEEFERDG&lid=LSTTVSGJ6YFUEEFERDGWANIEX&marketplace=FLIPKART&q=Sony+216+cm+%2885+inches%29+X85K+4K+Ultra+HD&store=ckf%2Fczl&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=d5150e94-419f-46e0-9485-c273702dc574.TVSGJ6YFUEEFERDG.SEARCH&ppt=sp&ppn=sp&ssid=ou0o4ged2o0000001684946808377&qH=ff92c322e3b417c6',
        'reliance_digital':'https://www.reliancedigital.in/sony-bravia-215-cm-85-inches-4k-ultra-hd-smart-led-google-tv-kd-85x85k-black-2022-model-with-dolby-vision-atmos-alexa-compatibility/p/493285616',
        'vijay_sales':'https://www.vijaysales.com/sony-x85k-ultra-hd-4k-smart-led-85-inch-215-cm-kd85x85k-2022-model-edition/21662'
    },
    6: {
        'title': 'Haier 258 L Refrigerator',
        'image': 'static/images/refri.jpg',
        'alt': 'Refrigerator image',
        'flipkart':'https://www.flipkart.com/haier-258-l-frost-free-double-door-3-star-convertible-refrigerator/p/itma2596b1a88059?pid=RFRGGUQU4R9ASHSE&lid=LSTRFRGGUQU4R9ASHSEPC2ZY6&marketplace=FLIPKART&q=Haier+258L+3+Star+Twin-Inverter+Frost+Free+Double+Door+Refrigerator&store=j9e%2Fabm%2Fhzg&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=b5994ea1-607d-4852-ae01-d2a509a5ab13.RFRGGUQU4R9ASHSE.SEARCH&ppt=sp&ppn=sp&ssid=fcnkrgk9yo0000001684946996163&qH=562198462cb57317',
        'reliance_digital':'https://www.reliancedigital.in/haier-258l-3-star-twin-inverter-frost-free-double-door-refrigerator-hef-25tds-brushline-silver-5-in-1-convertible-stabilizer-free-operation-/p/492664752',
        'vijay_sales':'https://www.vijaysales.com/haier-276-ltrs-3-star-frost-free-double-door-refrigerator-hrb2964cise-inox-steel/15135'
    },
    7: {
        'title': 'Whirlpool Washing Machine',
        'image': 'static/images/whirlpool.jpg',
        'alt': 'Whirlpool image',
        'flipkart':'https://www.flipkart.com/whirlpool-7-5-kg-fully-automatic-top-load-washing-machine-in-built-heater-grey/p/itm74cf8887ac4d7?pid=WMNGZJBXP6JSWG2V&lid=LSTWMNGZJBXP6JSWG2VZMRWR9&marketplace=FLIPKART&q=Whirlpool+7.5+Kg+5+Star+Bloom+Wash+Pro&store=j9e%2Fabm%2F8qx&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=7b61f96f-4bcd-4253-aac8-1da615bbec0b.WMNGZJBXP6JSWG2V.SEARCH&ppt=sp&ppn=sp&ssid=y2so75u5yo0000001684947293992&qH=84b1b164d0f99167',
        'reliance_digital':'https://www.reliancedigital.in/whirlpool-7-5-kg-5-star-fully-automatic-top-loading-washing-machine-360-bloomwash-pro-540-7-5-graphite-certified-no-1-in-cleaning-performance-with-hexa-bloom-impeller-/p/491666515',
        'vijay_sales':'https://www.vijaysales.com/whirlpool-7-5-kg-fully-automatic-top-load-washing-machine-360bwpro540h75g-graphite/11654'
    },
    8: {
        'title': 'BAJAJ Desert Air Cooler',
        'image': 'static/images/cooler.jpg',
        'alt': 'Cooler image',
        'flipkart':'https://www.flipkart.com/bajaj-90-l-desert-air-cooler/p/itmf55b9dc9b5c7f?pid=AICGYZGHPHH7G9VE&lid=LSTAICGYZGHPHH7G9VEBUQMFR&marketplace=FLIPKART&q=Bajaj+Wave+Air+Cooler+with+Turbo+Fan+Technology&store=j9e%2Fabm&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=73952287-25ac-46a2-ba8e-787301d712e8.AICGYZGHPHH7G9VE.SEARCH&ppt=sp&ppn=sp&ssid=rieer72bcw0000001684947594613&qH=a3e8f0dbdbc736ec',
        'reliance_digital':'https://www.reliancedigital.in/bajaj-dmh70-70-litres-desert-air-cooler-with-turbo-fan-technology/p/492664554',
        'vijay_sales':'https://www.vijaysales.com/bajaj-wave-air-cooler-with-turbo-fan-technology-3-level-speed-control-dmh60-white/23755'
    },
    9: {
        'title': 'Panasonic AC',
        'image': 'static/images/ac.jpg',
        'alt': 'Panasonic image',
        'flipkart':'https://www.flipkart.com/panasonic-convertible-7-in-1-additional-ai-mode-cooling-2023-model-2-ton-3-star-split-inverter-way-swing-pm-0-1-air-purification-filter-ac-wi-fi-connect-white/p/itm4370ddf99f550?pid=ACNGHHH2CVRPJEAY&lid=LSTACNGHHH2CVRPJEAYSKXLQR&marketplace=FLIPKART&q=Panasonic+2+Ton+%283+Star+-+Inverter%29+&store=j9e%2Fabm%2Fc54&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=3342d63a-b3e9-4a34-9ee6-72905351504f.ACNGHHH2CVRPJEAY.SEARCH&ppt=sp&ppn=sp&ssid=my6pvap3340000001684947789764&qH=7473ec61f4ef6845',
        'reliance_digital':'https://www.reliancedigital.in/panasonic-2t-3-star-7-in-1-convertible-inverter-split-ac-ku24zkyf1-shield-blu-durable-protection-r32-pm-0-1-filteration-2023-launch-/p/581110383',
        'vijay_sales':'https://www.vijaysales.com/panasonic-2-ton-3-star-inverter-split-ac-with-copper-condenser-csku24zkyf1/23985'
    }
}
        

@app.route('/', methods = ['POST', 'GET'])
def home():
    return render_template('index.html', product_list = product_list)


@app.route('/product/<int:pid>', methods = ['POST', 'GET'])
def product(pid):
    product = product_list[pid]
    product_name = product['title']

    flipkart_url = product['flipkart']
    reliance_digital_url = product['reliance_digital']
    vijay_sales_url = product['vijay_sales']

    if prices_cache[pid] == []:
        fp = get_price_from_flipkart(flipkart_url)
        rdp = get_price_from_reliance_digital(reliance_digital_url)
        vsp = get_price_from_vijay_sales(vijay_sales_url)
        prices_cache[pid] = [fp, rdp, vsp]

    flipkart_price = prices_cache[pid][0]
    reliance_digital_price = prices_cache[pid][1]
    vijay_sales_price = prices_cache[pid][2]

    return render_template(
        'product.html', 
        product_name=product_name, 
        flipkart_price=flipkart_price, 
        reliance_digital_price=reliance_digital_price, 
        vijay_sales_price=vijay_sales_price
    )
