#!/usr/bin/env python3
"""Build the event-year sweep plan: every conference series in the archive, extrapolated to the years it
ran (2006 onward = the first electronic DEF CON badge), plus badge-producing cons not yet in the archive.

Writes data/sweep_plan.json (one task per agent) and data/sweep_cons.json (con name -> event id base, so
discovery_to_stubs.py can file candidates under new events safely)."""
import json, os, re, yaml
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EV = yaml.safe_load(open(os.path.join(ROOT, "_data", "events.yml")))

tasks, cons = [], {}
def con(name, base, family, location=""):
    cons[name.lower()] = {"base": base, "family": family, "location": location}
def task(key, label, series, years, ids, angle, hints=""):
    tasks.append({"key": key, "label": label, "series": series, "years": years, "ids": ids, "angle": angle, "hints": hints})

# --- DEF CON, one task per year, extra angles for the badgelife-era years
con("DEF CON", "dc", "defcon", "Las Vegas, NV")
DC_ANGLES = {
 "all": "official badge, village/contest/party badges, SAOs, minibadges, kits and community badges",
 "badges": "the official badge, every village, contest, party, vendor and DC-group badge (Car Hacking, IoT, Wireless, Crypto & Privacy, Biohacking, AI, Aerospace, Hardware Hacking, Lockpick, Packet Hacking, Recon, Voting, Ham Radio villages; Queercon, DCZia, DC801, DC503, DC540, Hacker Jeopardy, Whose Slide, Toxic BBQ, Black Badge, Uber badge)",
 "saos": "SAOs / shitty add-ons: Hackaday.io projects, GitHub repos, Tindie/Etsy/Uberflux listings, the badge.life community sheets, SAO wall/showcase posts, maker recaps on Twitter/X, Bluesky, Mastodon",
 "indie": "independent/community badges, minibadges, kits and accessories: Kickstarter/Indiegogo campaigns, Hackaday.com and hackster coverage, r/badgelife and r/Defcon threads, DEF CON forum threads, YouTube badge roundups, badge.life archive pages",
}
for n in range(14, 35):
    y = 1992 + n
    angles = ["all"] if n <= 24 else (["badges", "saos"] if n == 25 else ["badges", "saos", "indie"])
    for a in angles:
        task(f"dc{n}-{a}", f"DEF CON {n} ({y}) — {a}", "DEF CON", [y], [f"dc{n}"], DC_ANGLES[a],
             "DEF CON is in Las Vegas every August (DC28 in 2020 was online as 'Safe Mode'). Event id is dc<number>.")

# --- Hackaday Supercon and Hackaday's other events
con("Hackaday Supercon", "supercon", "supercon", "Pasadena, CA"); con("Supercon", "supercon", "supercon", "Pasadena, CA")
for y in range(2015, 2027):
    task(f"supercon-{y}", f"Hackaday Supercon {y}", "Hackaday Supercon", [y], [f"supercon-{y}"],
         "the official Supercon badge, badge add-ons/SAOs/hacks, community badges and minibadges brought to Supercon, Supercon add-on contest entries",
         "Supercon 2015 was in San Francisco; 2016 onward Pasadena, CA (2020 = Remoticon online, 2021 = Remoticon online).")
con("Hackaday Europe", "hackaday-europe", "supercon", "Berlin, Germany"); con("Hackaday Berlin", "hackaday-berlin", "supercon", "Berlin, Germany"); con("Hackaday Belgrade", "hackaday-belgrade", "supercon", "Belgrade, Serbia")
task("hackaday-europe", "Hackaday Belgrade / Berlin / Europe (2016–2026)", "Hackaday Europe", [2016, 2018, 2023, 2024, 2025, 2026],
     ["hackaday-belgrade-2016", "hackaday-belgrade-2018", "hackaday-berlin-2023", "hackaday-europe-2024", "hackaday-europe-2025", "hackaday-europe-2026"],
     "the official conference badges and any add-ons or community badges for Hackaday Belgrade 2016 and 2018, Hackaday Berlin 2023, Hackaday Europe 2024, 2025 and 2026")

# --- SAINTCON (minibadge culture), BornHack, per year
con("SAINTCON", "saintcon", "other", "Utah")
for y in range(2014, 2027):
    task(f"saintcon-{y}", f"SAINTCON {y}", "SAINTCON", [y], [f"saintcon-{y}"],
         "the official SAINTCON badge, every minibadge (community, vendor, village, contest), SAOs and badge kits; sources: saintcon.org, minibadge.dev / minibadge lists, Hackaday.io, GitHub, Twitter/X, Discord recaps, hackerboxes, Utah hackerspace pages",
         "SAINTCON is Utah's security con (Provo/Salt Lake City), every autumn. Minibadges are 1x1 inch boards that snap onto the badge.")
con("BornHack", "bornhack", "camp", "Denmark")
for y in range(2016, 2027):
    task(f"bornhack-{y}", f"BornHack {y}", "BornHack", [y], [f"bornhack-{y}"],
         "the official BornHack badge, badge add-ons, workshop kits and community badges; sources: bornhack.dk, github.com/bornhack, hackaday.io, blog posts, Mastodon",
         "BornHack is a Danish hacker camp held every August (Bornholm 2016–2018, Funen from 2019).")

# --- camps and camp-adjacent series, one task per series
con("EMF Camp", "emf-camp", "camp", "Eastnor, UK"); con("Electromagnetic Field", "emf-camp", "camp", "Eastnor, UK")
task("emf-badges", "EMF Camp official badges 2012–2026", "EMF Camp", [2012, 2014, 2016, 2018, 2022, 2024, 2026], [f"emf-camp-{y}" for y in (2012, 2014, 2016, 2018, 2022, 2024, 2026)],
     "the official TiLDA badges (TiLDA, TiLDA MKe, MK3, MK4, TiDAL, Tildagon) and their official add-ons")
task("emf-addons", "EMF Camp add-ons, hats and community badges", "EMF Camp", [2016, 2018, 2022, 2024, 2026], [f"emf-camp-{y}" for y in (2016, 2018, 2022, 2024, 2026)],
     "TiLDA/TiDAL/Tildagon hexpansions, hats, add-on boards, community badges and village badges brought to EMF; sources: badge.emfcamp.org, hexpansion lists, GitHub, wiki.emfcamp.org, Mastodon, Hackaday.io")
con("Chaos Communication Camp", "cccamp", "camp", "Mildenberg, Germany"); con("CCCamp", "cccamp", "camp", "Mildenberg, Germany")
task("cccamp", "Chaos Communication Camp 2007–2023", "Chaos Communication Camp", [2007, 2011, 2015, 2019, 2023], [f"cccamp-{y}" for y in (2007, 2011, 2015, 2019, 2023)],
     "official camp badges (Sputnik 2007, r0ket 2011, rad1o 2015, card10 2019, flow3r 2023) and their add-ons/community boards")
con("Chaos Communication Congress", "ccc-congress", "camp", "Germany"); con("GPN", "gpn", "camp", "Karlsruhe, Germany"); con("Easterhegg", "easterhegg", "camp", "Germany"); con("MRMCD", "mrmcd", "camp", "Darmstadt, Germany")
task("ccc-adjacent", "CCC-adjacent events: Congress (3xC3), GPN, Easterhegg, MRMCD, Datenspuren", "Chaos Communication Congress", list(range(2010, 2027)), [],
     "electronic badges, blinky boards and add-ons made for or brought to Chaos Communication Congress (3xC3), GPN, Easterhegg, MRMCD or Datenspuren; sources: events.ccc.de, github, hackaday.io, chaos.social")
for nm, base, loc in (("HAR", "har", "Vierhouten, NL"), ("OHM", "ohm", "Geestmerambacht, NL"), ("SHA", "sha", "Zeewolde, NL"), ("MCH", "mch", "Zeewolde, NL"), ("WHY", "why", "Biddinghuizen, NL")): con(nm, base, "camp", loc)
task("dutch-camps", "Dutch camps HAR 2009, OHM 2013, SHA 2017, MCH 2022, WHY 2025", "Dutch hacker camps", [2009, 2013, 2017, 2022, 2025], ["har-2009", "ohm-2013", "sha-2017", "mch-2022", "why-2025"],
     "official camp badges (badge.team lineage) and their add-ons, hatchery apps aside; community badges brought to the camp")
con("CampZone", "campzone", "camp", "Netherlands"); con("HackerHotel", "hackerhotel", "camp", "Netherlands"); con("Fri3d Camp", "fri3d", "camp", "Belgium"); con("Fri3d", "fri3d", "camp", "Belgium")
task("campzone", "CampZone 2019–2025", "CampZone", list(range(2019, 2026)), [f"campzone-{y}" for y in range(2019, 2026)], "official CampZone badges (badge.team) and add-ons")
task("hackerhotel", "HackerHotel 2019–2026", "HackerHotel", [2019, 2020, 2022, 2023, 2024, 2025, 2026], [f"hackerhotel-{y}" for y in (2019, 2020, 2022, 2023, 2024, 2025, 2026)], "official HackerHotel badges and add-ons")
task("fri3d", "Fri3d Camp 2014–2026", "Fri3d Camp", [2014, 2016, 2018, 2022, 2024, 2026], [f"fri3d-{y}" for y in (2014, 2016, 2018, 2022, 2024, 2026)], "official Fri3d Camp badges and add-ons/kits (fri3d.be, github.com/Fri3dCamp)")

# --- other recurring cons already in the archive, one task per series (two for THOTCON)
con("THOTCON", "thotcon", "other", "Chicago, IL")
task("thotcon-a", "THOTCON 0x1–0x8 (2010–2017)", "THOTCON", list(range(2010, 2018)), [f"thotcon-{y}" for y in range(2010, 2018)], "official THOTCON badges and any add-ons or community badges", "THOTCON numbers editions in hex: 0x1 = 2010 … 0x8 = 2017.")
task("thotcon-b", "THOTCON 0x9–0xD (2018–2025)", "THOTCON", [2018, 2019, 2022, 2023, 2024, 2025], [f"thotcon-{y}" for y in (2018, 2019, 2022, 2023, 2024, 2025)], "official THOTCON badges, SAOs and community badges", "0x9 = 2018, 0xA = 2019, 0xB = 2022, 0xC = 2023, 0xD = 2025; confirm whether anything happened in 2024.")
con("CypherCon", "cyphercon", "other", "Milwaukee, WI")
task("cyphercon", "CypherCon 2016–2026", "CypherCon", list(range(2016, 2027)), [f"cyphercon-{y}" for y in range(2016, 2027)], "official CypherCon badges (electronic, puzzle), SAOs and community badges")
con("CarolinaCon", "carolinacon", "other", "North Carolina")
task("carolinacon", "CarolinaCon 2016–2026", "CarolinaCon", list(range(2016, 2027)), ["carolinacon-16", "carolinacon-online-2021"], "official CarolinaCon badges and community badges", "Existing ids: carolinacon-16 (2020) and carolinacon-online-2021; for other years use event_hint 'CarolinaCon <year>'.")
con("NorthSec", "northsec", "other", "Montreal, QC")
task("northsec", "NorthSec 2013–2026", "NorthSec", list(range(2013, 2027)), [f"northsec-{y}" for y in range(2013, 2027)], "official NorthSec badges and any add-ons")
con("Queercon", "queercon", "other", "Las Vegas, NV"); con("TiaraCon", "tiaracon", "other", "Las Vegas, NV")
task("queercon", "Queercon 2011–2026 and TiaraCon 2016–2017", "Queercon", list(range(2011, 2027)), [f"queercon-{y}" for y in range(2011, 2027)] + ["tiaracon-2016", "tiaracon-2017"], "Queercon badges (each year's badge, numbered Queercon 8 … ), Queercon add-ons, TiaraCon badges", "Queercon runs during DEF CON week; file under queercon-<year>, not dc<n>.")
con("ShmooCon", "shmoocon", "other", "Washington, DC")
task("shmoocon", "ShmooCon 2006–2025", "ShmooCon", [y for y in range(2006, 2026) if y != 2021], [f"shmoocon-{y}" for y in range(2006, 2026) if y != 2021], "ShmooCon badges (including barcode/RFID/electronic years), Shmooganography and community badges")
con("HOPE", "hope", "other", "New York, NY")
task("hope", "HOPE 2008–2026", "HOPE", [2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026], [f"hope-{y}" for y in (2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026)], "official HOPE badges (RFID badges 2008/2010, HOPE X, XI, XII, 2020, 2022, XV, 16) and community badges")
con("OSHWDem", "oshwdem", "other", "A Coruña, Spain")
task("oshwdem", "OSHWDem 2013–2025", "OSHWDem", list(range(2013, 2026)), [f"oshwdem-{y}" for y in range(2013, 2026)], "OSHWDem badges and kits")

# --- BSides: one task per city already in the archive, grouped tasks for well-known badge cities
BS_PRESENT = [("Cape Town", "bsides-cape-town"), ("Orlando", "bsides-orlando"), ("Jacksonville", "bsides-jacksonville"), ("Rochester", "bsides-rochester"),
              ("Iowa", "bsides-iowa"), ("DFW", "bsidesdfw"), ("Adelaide", "bsides-adelaide"), ("Puerto Rico", "bsidespr"), ("Salt Lake City", "bsides-slc"), ("San Diego", "bsides-san-diego"), ("Tallinn", "bsides-tallinn")]
for city, base in BS_PRESENT:
    con(f"BSides {city}", base, "bsides")
    task(f"bsides-{base}", f"BSides {city}, all years", "BSides " + city, list(range(2012, 2027)), [k for k in EV if k.startswith(base + "-")], f"every BSides {city} conference badge (electronic or notable), SAO and community badge, by year")
BS_GROUPS = [["Las Vegas", "San Francisco", "Seattle"], ["Canberra", "Melbourne", "Perth"], ["Philadelphia", "Delaware", "Charm"], ["Portland", "Denver", "Boise"],
             ["Augusta", "Tampa", "Nashville"], ["Huntsville", "Atlanta", "Charleston"], ["Boston", "NoVA", "Ottawa"], ["Kansas City", "Cleveland", "Columbus"],
             ["Detroit", "Chicago", "Vancouver"], ["London", "Manchester", "Munich"], ["Singapore", "Tokyo", "Dublin"]]
for g in BS_GROUPS:
    for city in g: con(f"BSides {city}", "bsides-" + re.sub(r"[^a-z0-9]+", "-", city.lower().split(" (")[0]).strip("-"), "bsides")
    task("bsides-" + re.sub(r"[^a-z0-9]+", "-", g[0].lower()), "BSides " + " / ".join(g), "BSides", list(range(2012, 2027)), [], f"every conference badge, SAO and community badge made for BSides {', '.join(g)} in any year")
for nm, base in (("HITBSecConf", "hitb"), ("HITB SecConf", "hitb"), ("Hack In The Box", "hitb"), ("Sec-T", "sec-t"), ("SEC-T", "sec-t"), ("Hackers Teaching Hackers", "hackers-teaching-hackers"), ("HTH", "hackers-teaching-hackers"),
                 ("PHDays Fest", "phdays"), ("HITCON CMT", "hitcon"), ("Roadsec", "roadsec"), ("RoadSec", "roadsec"), ("DEF CON China Beta", "def-con-china")): con(nm, base, "other")
# abbreviations agents use for BSides cities, so "BSidesPDX 2017" and "BSides Portland 2017" land on one event id
for abbr, base in {"bsidespdx": "bsides-portland", "bsideskc": "bsides-kansas-city", "bsidesslc": "bsides-slc", "bsides salt lake city": "bsides-slc", "bsides slc": "bsides-slc",
                   "bsideslv": "bsides-las-vegas", "bsidessf": "bsides-san-francisco", "bsidescbr": "bsides-canberra", "bsidesroc": "bsides-rochester", "bsidesjax": "bsides-jacksonville",
                   "bsideschs": "bsides-charleston", "bsidesphilly": "bsides-philadelphia", "bsidesmuc": "bsides-munich", "bsidesbos": "bsides-boston", "bsidesstl": "bsides-st-louis",
                   "bsides st. louis": "bsides-st-louis", "bsides st louis": "bsides-st-louis", "bsidescle": "bsides-cleveland", "bsidesnash": "bsides-nashville", "bsideshsv": "bsides-huntsville",
                   "bsidestpa": "bsides-tampa", "bsidesatl": "bsides-atlanta", "bsidesnova": "bsides-nova", "bsidesorl": "bsides-orlando", "bsidesdc": "bsides-dc", "bsides dc": "bsides-dc",
                   "bsidesla": "bsides-los-angeles", "bsides los angeles": "bsides-los-angeles", "bsidesctba": "bsides-cape-town", "bsides ct": "bsides-cape-town", "bsidesadl": "bsides-adelaide",
                   "bsidesmel": "bsides-melbourne", "bsidesperth": "bsides-perth", "bsidesbne": "bsides-brisbane", "bsides brisbane": "bsides-brisbane", "bsides sydney": "bsides-sydney",
                   "bsidessd": "bsides-san-diego", "bsidesyyc": "bsides-calgary", "bsides calgary": "bsides-calgary", "bsides edmonton": "bsides-edmonton", "bsidesto": "bsides-toronto", "bsides toronto": "bsides-toronto",
                   "bsides dfw": "bsidesdfw", "bsides puerto rico": "bsidespr", "bsidespr": "bsidespr", "bsides pr": "bsidespr", "bsides cymru": "bsides-cymru", "bsides leeds": "bsides-leeds",
                   "bsides manchester": "bsides-manchester", "bsides newcastle": "bsides-newcastle", "bsides bristol": "bsides-bristol", "bsides cheltenham": "bsides-cheltenham", "bsides exeter": "bsides-exeter",
                   "bsides zurich": "bsides-zurich", "bsides lisbon": "bsides-lisbon", "bsides athens": "bsides-athens", "bsides delhi": "bsides-delhi", "bsides bangalore": "bsides-bangalore",
                   "bsides tokyo": "bsides-tokyo", "bsides tallinn": "bsides-tallinn", "bsides orlando": "bsides-orlando", "bsides rochester": "bsides-rochester", "bsides iowa": "bsides-iowa"}.items():
    con(abbr, base, "bsides")
task("bsides-any", "BSides badges anywhere else", "BSides", list(range(2012, 2027)), [], "BSides badges from any other city worldwide (search 'BSides badge' by year, github 'bsides badge', hackaday.io 'bsides', badge.team, Tindie)")

# --- badge-producing cons not in the archive yet (grouped by region/affinity)
OTHERS = [
 (["LayerOne", "ShellCon", "CactusCon"], "Los Angeles, CA|Los Angeles, CA|Arizona"),
 (["DerbyCon", "GrrCON", "CircleCityCon"], "Louisville, KY|Grand Rapids, MI|Indianapolis, IN"),
 (["Kernelcon", "Wild West Hackin' Fest", "DakotaCon"], "Omaha, NE|Deadwood, SD|Madison, SD"),
 (["ToorCon", "ToorCamp", "HushCon"], "San Diego, CA|Washington|Seattle, WA"),
 (["Blue Team Con", "Hackers Teaching Hackers", "Texas Cyber Summit"], "Chicago, IL|Columbus, OH|Texas"),
 (["RVAsec", "Hack Red Con", "Hack West"], "Richmond, VA|Louisville, KY|"),
 (["DC801", "DC540", "DC503", "DC303"], "Salt Lake City, UT|Baltimore, MD|Portland, OR|Denver, CO"),
 (["DC404", "DC858", "DC406", "DC612", "DC414", "DC416"], "Atlanta, GA|San Diego, CA|Montana|Minneapolis, MN|Milwaukee, WI|Toronto, ON"),
 (["DEF CON China"], "Beijing, China"),
 (["Kiwicon", "CrikeyCon", "Ruxcon"], "Wellington, NZ|Brisbane, AU|Melbourne, AU"),
 (["Troopers", "HITB", "Nullcon"], "Heidelberg, Germany|Amsterdam, NL|Goa, India"),
 (["Disobey", "Sec-T", "T2"], "Helsinki, Finland|Stockholm, Sweden|Helsinki, Finland"),
 (["BruCON", "Hack.lu", "leHACK"], "Belgium|Luxembourg|Paris, France"),
 (["44CON", "SteelCon", "Securi-Tay"], "London, UK|Sheffield, UK|Dundee, UK"),
 (["BalCCon", "Hacktivity", "Insomni'hack"], "Novi Sad, Serbia|Budapest, Hungary|Geneva, Switzerland"),
 (["HITCON", "POC", "AVTokyo"], "Taipei, Taiwan|Seoul, Korea|Tokyo, Japan"),
 (["Ekoparty", "H2HC", "Roadsec"], "Buenos Aires, Argentina|São Paulo, Brazil|Brazil"),
 (["Open Sauce", "Maker Faire", "Teardown"], "San Francisco, CA||Portland, OR"),
 (["Navaja Negra", "RootedCON", "h-c0n"], "Albacete, Spain|Madrid, Spain|Madrid, Spain"),
 (["PHDays", "ZeroNights", "OFFZONE"], "Moscow, Russia|Moscow, Russia|Moscow, Russia"),
 (["Hackfest", "SecTor", "Converge"], "Quebec City, QC|Toronto, ON|Detroit, MI"),
 (["NolaCon", "PancakesCon", "Hackers Next Door"], "New Orleans, LA|Online|New York, NY"),
]
for names, locs in OTHERS:
    for n, l in zip(names, locs.split("|")):
        con(n, re.sub(r"[^a-z0-9]+", "-", n.lower()).strip("-"), "other", l)
    task("con-" + re.sub(r"[^a-z0-9]+", "-", names[0].lower()).strip("-"), " / ".join(names), names[0], list(range(2006, 2027)), [],
         f"every electronic or notable conference badge, SAO, minibadge or kit made for {', '.join(names)} in any year; confirm each event's year, dates and city")

# --- general sweeps by year band (con-agnostic sources)
for a, b in ((2006, 2015), (2016, 2019), (2020, 2022), (2023, 2024), (2025, 2026)):
    task(f"general-{a}", f"General sweep {a}–{b}", "general", list(range(a, b + 1)), [],
         "badges, SAOs and minibadges from ANY conference in these years that the archive lacks: hackaday.io tag/search 'conference badge' and 'SAO', badge.life archive pages, r/badgelife top posts, Hackaday.com badge coverage, GitHub topic 'badgelife' / 'conference-badge' / 'sao', Tindie 'badge' and 'SAO' categories, Kickstarter badges")

json.dump(tasks, open(os.path.join(ROOT, "data", "sweep_plan.json"), "w"), indent=1, ensure_ascii=False)
json.dump(cons, open(os.path.join(ROOT, "data", "sweep_cons.json"), "w"), indent=1, ensure_ascii=False)
print(len(tasks), "tasks;", len(cons), "con names")
