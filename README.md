# FCDO Travel Advice Status

This repository automatically tracks the UK Foreign, Commonwealth & Development Office (FCDO) travel advice status for all listed countries. The table below is updated daily via a GitHub Action.

## Traffic Light System

The status column uses a traffic light system based on the following rules:

*   🔴 **Red:** FCDO advises against **all travel** to the **whole country** (applies if `avoid_all_travel_to_whole_country` is present, taking precedence over other alerts).
*   🔴* **Red with Asterisk:** FCDO advises against **all travel** to **parts** of the country (applies if `avoid_all_travel_to_parts` is present and `avoid_all_travel_to_whole_country` is NOT present).
*   🟡 **Yellow:** FCDO advises against **all but essential travel** (applies if `avoid_all_but_essential_travel_to_parts` or `avoid_all_but_essential_travel_to_whole_country` is present), **and** no Red-level warnings are present.
*   🟢 **Green:** No FCDO travel warnings apply (the API returns an empty list for `alert_status`).
*   ❓ **Question Mark:** An error occurred fetching/processing data, the `alert_status` was missing or invalid, or contained unrecognized values.

Refer to the linked FCDO advice page for full details on any warnings.

---

## Travel Advice Table

<!-- FCDO_TABLE_START -->
| Status | Country | FCDO Advice |
|:------:|---------|-------------|
| 🔴* | [Azerbaijan](https://www.gov.uk/foreign-travel-advice/azerbaijan) | avoid_all_travel_to_parts, avoid_all_but_essential_travel_to_parts |
| 🟡 | [Papua New Guinea](https://www.gov.uk/foreign-travel-advice/papua-new-guinea) | avoid_all_but_essential_travel_to_parts |
| 🟢 | [Federated States of Micronesia](https://www.gov.uk/foreign-travel-advice/federated-states-of-micronesia) | No specific alerts |
| 🟢 | [China](https://www.gov.uk/foreign-travel-advice/china) | No specific alerts |
| 🟢 | [Botswana](https://www.gov.uk/foreign-travel-advice/botswana) | No specific alerts |
| 🔴* | [Burundi](https://www.gov.uk/foreign-travel-advice/burundi) | avoid_all_travel_to_parts, avoid_all_but_essential_travel_to_parts |
| 🟡 | [Bangladesh](https://www.gov.uk/foreign-travel-advice/bangladesh) | avoid_all_but_essential_travel_to_parts |
| 🔴 | [Indonesia](https://www.gov.uk/foreign-travel-advice/indonesia) | avoid_all_travel_to_parts |
| 🔴 | [Philippines](https://www.gov.uk/foreign-travel-advice/philippines) | avoid_all_travel_to_parts |
| 🟢 | [New Caledonia](https://www.gov.uk/foreign-travel-advice/new-caledonia) | No specific alerts |
| 🟡 | [Thailand](https://www.gov.uk/foreign-travel-advice/thailand) | avoid_all_but_essential_travel_to_parts |
| 🟢 | [Mauritius](https://www.gov.uk/foreign-travel-advice/mauritius) | No specific alerts |
| 🔴 | [Turkey](https://www.gov.uk/foreign-travel-advice/turkey) | avoid_all_travel_to_parts |
| 🔴* | [Libya](https://www.gov.uk/foreign-travel-advice/libya) | avoid_all_travel_to_parts, avoid_all_but_essential_travel_to_parts |
| 🟢 | [Gabon](https://www.gov.uk/foreign-travel-advice/gabon) | No specific alerts |
| 🟢 | [Antarctica/British Antarctic Territory](https://www.gov.uk/foreign-travel-advice/antarctica-british-antarctic-territory) | No specific alerts |
| 🔴 | [South Sudan](https://www.gov.uk/foreign-travel-advice/south-sudan) | avoid_all_travel_to_whole_country |
| 🔴 | [Sudan](https://www.gov.uk/foreign-travel-advice/sudan) | avoid_all_travel_to_parts |
| 🔴 | [Democratic Republic of the Congo](https://www.gov.uk/foreign-travel-advice/democratic-republic-of-the-congo) | avoid_all_travel_to_parts |
| 🟡 | [Angola](https://www.gov.uk/foreign-travel-advice/angola) | avoid_all_but_essential_travel_to_parts |
| 🔴 | [Afghanistan](https://www.gov.uk/foreign-travel-advice/afghanistan) | avoid_all_travel_to_whole_country |
| 🟢 | [Cyprus](https://www.gov.uk/foreign-travel-advice/cyprus) | No specific alerts |
| 🟢 | [Australia](https://www.gov.uk/foreign-travel-advice/australia) | No specific alerts |
| 🟢 | [Tonga](https://www.gov.uk/foreign-travel-advice/tonga) | No specific alerts |
| 🔴* | [Myanmar (Burma)](https://www.gov.uk/foreign-travel-advice/myanmar) | avoid_all_travel_to_parts, avoid_all_but_essential_travel_to_parts |
| 🟢 | [Portugal](https://www.gov.uk/foreign-travel-advice/portugal) | No specific alerts |
| 🟢 | [Romania](https://www.gov.uk/foreign-travel-advice/romania) | No specific alerts |
| 🟢 | [Slovakia](https://www.gov.uk/foreign-travel-advice/slovakia) | No specific alerts |
| 🟢 | [South Africa](https://www.gov.uk/foreign-travel-advice/south-africa) | No specific alerts |
| 🟡 | [Mexico](https://www.gov.uk/foreign-travel-advice/mexico) | avoid_all_but_essential_travel_to_parts |
| 🟢 | [Sweden](https://www.gov.uk/foreign-travel-advice/sweden) | No specific alerts |
| 🟢 | [Iceland](https://www.gov.uk/foreign-travel-advice/iceland) | No specific alerts |
| 🟢 | [Norway](https://www.gov.uk/foreign-travel-advice/norway) | No specific alerts |
| 🟢 | [Liechtenstein](https://www.gov.uk/foreign-travel-advice/liechtenstein) | No specific alerts |
| 🟢 | [Switzerland](https://www.gov.uk/foreign-travel-advice/switzerland) | No specific alerts |
| 🟡 | [Tanzania](https://www.gov.uk/foreign-travel-advice/tanzania) | avoid_all_but_essential_travel_to_parts |
| 🟢 | [Austria](https://www.gov.uk/foreign-travel-advice/austria) | No specific alerts |
| 🟢 | [Bulgaria](https://www.gov.uk/foreign-travel-advice/bulgaria) | No specific alerts |
| 🟢 | [Croatia](https://www.gov.uk/foreign-travel-advice/croatia) | No specific alerts |
| 🟢 | [Czech Republic](https://www.gov.uk/foreign-travel-advice/czech-republic) | No specific alerts |
| 🟢 | [Denmark](https://www.gov.uk/foreign-travel-advice/denmark) | No specific alerts |
| 🟢 | [France](https://www.gov.uk/foreign-travel-advice/france) | No specific alerts |
| 🟢 | [Lithuania](https://www.gov.uk/foreign-travel-advice/lithuania) | No specific alerts |
| 🟢 | [Poland](https://www.gov.uk/foreign-travel-advice/poland) | No specific alerts |
| 🟢 | [Germany](https://www.gov.uk/foreign-travel-advice/germany) | No specific alerts |
| 🟢 | [Estonia](https://www.gov.uk/foreign-travel-advice/estonia) | No specific alerts |
| 🟢 | [Finland](https://www.gov.uk/foreign-travel-advice/finland) | No specific alerts |
| 🟢 | [Hungary](https://www.gov.uk/foreign-travel-advice/hungary) | No specific alerts |
| 🟢 | [Greece](https://www.gov.uk/foreign-travel-advice/greece) | No specific alerts |
| 🟢 | [Latvia](https://www.gov.uk/foreign-travel-advice/latvia) | No specific alerts |
| 🟢 | [Luxembourg](https://www.gov.uk/foreign-travel-advice/luxembourg) | No specific alerts |
| 🟢 | [Malta](https://www.gov.uk/foreign-travel-advice/malta) | No specific alerts |
| 🟢 | [Netherlands](https://www.gov.uk/foreign-travel-advice/netherlands) | No specific alerts |
| 🟢 | [Brunei](https://www.gov.uk/foreign-travel-advice/brunei) | No specific alerts |
| 🟢 | [Taiwan](https://www.gov.uk/foreign-travel-advice/taiwan) | No specific alerts |
| 🟢 | [Kyrgyzstan](https://www.gov.uk/foreign-travel-advice/kyrgyzstan) | No specific alerts |
| 🟡 | [Malaysia](https://www.gov.uk/foreign-travel-advice/malaysia) | avoid_all_but_essential_travel_to_parts |
| 🟡 | [Ecuador](https://www.gov.uk/foreign-travel-advice/ecuador) | avoid_all_but_essential_travel_to_parts |
| 🟡 | [Peru](https://www.gov.uk/foreign-travel-advice/peru) | avoid_all_but_essential_travel_to_parts |
| 🔴* | [Pakistan](https://www.gov.uk/foreign-travel-advice/pakistan) | avoid_all_travel_to_parts, avoid_all_but_essential_travel_to_parts |
| 🔴 | [Saudi Arabia](https://www.gov.uk/foreign-travel-advice/saudi-arabia) | avoid_all_travel_to_parts |
| 🟢 | [South Korea](https://www.gov.uk/foreign-travel-advice/south-korea) | No specific alerts |
| 🟡 | [Rwanda](https://www.gov.uk/foreign-travel-advice/rwanda) | avoid_all_but_essential_travel_to_parts |
| 🔴 | [Egypt](https://www.gov.uk/foreign-travel-advice/egypt) | avoid_all_travel_to_parts |
| 🟡 | [Brazil](https://www.gov.uk/foreign-travel-advice/brazil) | avoid_all_but_essential_travel_to_parts |
| 🟢 | [Oman](https://www.gov.uk/foreign-travel-advice/oman) | No specific alerts |
| 🟢 | [Madagascar](https://www.gov.uk/foreign-travel-advice/madagascar) | No specific alerts |
| 🟢 | [Slovenia](https://www.gov.uk/foreign-travel-advice/slovenia) | No specific alerts |
| 🟢 | [United Arab Emirates](https://www.gov.uk/foreign-travel-advice/united-arab-emirates) | No specific alerts |
| 🟢 | [Spain](https://www.gov.uk/foreign-travel-advice/spain) | No specific alerts |
| 🔴 | [India](https://www.gov.uk/foreign-travel-advice/india) | avoid_all_travel_to_parts |
| 🟡 | [Ghana](https://www.gov.uk/foreign-travel-advice/ghana) | avoid_all_but_essential_travel_to_parts |
| 🟡 | [Colombia](https://www.gov.uk/foreign-travel-advice/colombia) | avoid_all_but_essential_travel_to_parts |
| 🟢 | [Belgium](https://www.gov.uk/foreign-travel-advice/belgium) | No specific alerts |
| 🟢 | [Italy](https://www.gov.uk/foreign-travel-advice/italy) | No specific alerts |
| 🔴 | [Côte d'Ivoire](https://www.gov.uk/foreign-travel-advice/cote-d-ivoire) | avoid_all_travel_to_parts |
| 🔴 | [Togo](https://www.gov.uk/foreign-travel-advice/togo) | avoid_all_travel_to_parts |
| 🟢 | [Pitcairn Island](https://www.gov.uk/foreign-travel-advice/pitcairn-island) | No specific alerts |
| 🔴* | [Lebanon](https://www.gov.uk/foreign-travel-advice/lebanon) | avoid_all_travel_to_parts, avoid_all_but_essential_travel_to_parts |
| 🟢 | [Tajikistan](https://www.gov.uk/foreign-travel-advice/tajikistan) | No specific alerts |
| 🟢 | [USA](https://www.gov.uk/foreign-travel-advice/usa) | No specific alerts |
| 🟢 | [Trinidad and Tobago](https://www.gov.uk/foreign-travel-advice/trinidad-and-tobago) | No specific alerts |
| 🔴 | [Mauritania](https://www.gov.uk/foreign-travel-advice/mauritania) | avoid_all_travel_to_parts |
| 🟢 | [Vietnam](https://www.gov.uk/foreign-travel-advice/vietnam) | No specific alerts |
| 🟢 | [Cook Islands, Tokelau and Niue](https://www.gov.uk/foreign-travel-advice/cook-islands-tokelau-and-niue) | No specific alerts |
| 🟢 | [Namibia](https://www.gov.uk/foreign-travel-advice/namibia) | No specific alerts |
| 🟡 | [Laos](https://www.gov.uk/foreign-travel-advice/laos) | avoid_all_but_essential_travel_to_parts |
| 🟢 | [Zimbabwe](https://www.gov.uk/foreign-travel-advice/zimbabwe) | No specific alerts |
| 🟢 | [Sierra Leone](https://www.gov.uk/foreign-travel-advice/sierra-leone) | No specific alerts |
| 🔴 | [Burkina Faso](https://www.gov.uk/foreign-travel-advice/burkina-faso) | avoid_all_travel_to_parts |
| 🔴 | [Belarus](https://www.gov.uk/foreign-travel-advice/belarus) | avoid_all_travel_to_whole_country |
| 🟢 | [Barbados](https://www.gov.uk/foreign-travel-advice/barbados) | No specific alerts |
| 🟢 | [Belize](https://www.gov.uk/foreign-travel-advice/belize) | No specific alerts |
| 🟢 | [Grenada](https://www.gov.uk/foreign-travel-advice/grenada) | No specific alerts |
| 🟢 | [Zambia](https://www.gov.uk/foreign-travel-advice/zambia) | No specific alerts |
| 🟢 | [Lesotho](https://www.gov.uk/foreign-travel-advice/lesotho) | No specific alerts |
| 🟢 | [Dominican Republic](https://www.gov.uk/foreign-travel-advice/dominican-republic) | No specific alerts |
| 🔴 | [Georgia](https://www.gov.uk/foreign-travel-advice/georgia) | avoid_all_travel_to_parts |
| 🟢 | [Qatar](https://www.gov.uk/foreign-travel-advice/qatar) | No specific alerts |
| 🔴 | [Eritrea](https://www.gov.uk/foreign-travel-advice/eritrea) | avoid_all_travel_to_parts |
| 🟢 | [Serbia](https://www.gov.uk/foreign-travel-advice/serbia) | No specific alerts |
| 🟢 | [Panama](https://www.gov.uk/foreign-travel-advice/panama) | No specific alerts |
| 🟢 | [Albania](https://www.gov.uk/foreign-travel-advice/albania) | No specific alerts |
| 🔴 | [Nigeria](https://www.gov.uk/foreign-travel-advice/nigeria) | avoid_all_travel_to_parts |
| 🟢 | [Dominica](https://www.gov.uk/foreign-travel-advice/dominica) | No specific alerts |
| 🟢 | [Bhutan](https://www.gov.uk/foreign-travel-advice/bhutan) | No specific alerts |
| 🟢 | [British Indian Ocean Territory](https://www.gov.uk/foreign-travel-advice/british-indian-ocean-territory) | No specific alerts |
| 🟢 | [Cambodia](https://www.gov.uk/foreign-travel-advice/cambodia) | No specific alerts |
| 🟢 | [Comoros](https://www.gov.uk/foreign-travel-advice/comoros) | No specific alerts |
| 🟢 | [Fiji](https://www.gov.uk/foreign-travel-advice/fiji) | No specific alerts |
| 🟢 | [French Polynesia](https://www.gov.uk/foreign-travel-advice/french-polynesia) | No specific alerts |
| 🟢 | [Hong Kong](https://www.gov.uk/foreign-travel-advice/hong-kong) | No specific alerts |
| 🟢 | [Kazakhstan](https://www.gov.uk/foreign-travel-advice/kazakhstan) | No specific alerts |
| 🟢 | [Kiribati](https://www.gov.uk/foreign-travel-advice/kiribati) | No specific alerts |
| 🟢 | [Macao](https://www.gov.uk/foreign-travel-advice/macao) | No specific alerts |
| 🟢 | [Marshall Islands](https://www.gov.uk/foreign-travel-advice/marshall-islands) | No specific alerts |
| 🟢 | [Mongolia](https://www.gov.uk/foreign-travel-advice/mongolia) | No specific alerts |
| 🟢 | [Nauru](https://www.gov.uk/foreign-travel-advice/nauru) | No specific alerts |
| 🟢 | [New Zealand](https://www.gov.uk/foreign-travel-advice/new-zealand) | No specific alerts |
| 🟡 | [North Korea](https://www.gov.uk/foreign-travel-advice/north-korea) | avoid_all_but_essential_travel_to_whole_country |
| 🟢 | [Seychelles](https://www.gov.uk/foreign-travel-advice/seychelles) | No specific alerts |
| 🟢 | [Singapore](https://www.gov.uk/foreign-travel-advice/singapore) | No specific alerts |
| 🟢 | [Solomon Islands](https://www.gov.uk/foreign-travel-advice/solomon-islands) | No specific alerts |
| 🟢 | [Sri Lanka](https://www.gov.uk/foreign-travel-advice/sri-lanka) | No specific alerts |
| 🟢 | [Timor-Leste](https://www.gov.uk/foreign-travel-advice/timor-leste) | No specific alerts |
| 🟢 | [Turkmenistan](https://www.gov.uk/foreign-travel-advice/turkmenistan) | No specific alerts |
| 🟢 | [Equatorial Guinea](https://www.gov.uk/foreign-travel-advice/equatorial-guinea) | No specific alerts |
| 🟢 | [Eswatini](https://www.gov.uk/foreign-travel-advice/eswatini) | No specific alerts |
| 🟢 | [The Gambia](https://www.gov.uk/foreign-travel-advice/the-gambia) | No specific alerts |
| 🟢 | [Guinea-Bissau](https://www.gov.uk/foreign-travel-advice/guinea-bissau) | No specific alerts |
| 🟡 | [Kenya](https://www.gov.uk/foreign-travel-advice/kenya) | avoid_all_but_essential_travel_to_parts |
| 🟢 | [French Guiana](https://www.gov.uk/foreign-travel-advice/french-guiana) | No specific alerts |
| 🟢 | [Guyana](https://www.gov.uk/foreign-travel-advice/guyana) | No specific alerts |
| 🟢 | [Paraguay](https://www.gov.uk/foreign-travel-advice/paraguay) | No specific alerts |
| 🟢 | [South Georgia and the South Sandwich Islands](https://www.gov.uk/foreign-travel-advice/south-georgia-and-south-sandwich-islands) | No specific alerts |
| 🟢 | [St Helena, Ascension and Tristan da Cunha](https://www.gov.uk/foreign-travel-advice/st-helena-ascension-and-tristan-da-cunha) | No specific alerts |
| 🟢 | [Suriname](https://www.gov.uk/foreign-travel-advice/suriname) | No specific alerts |
| 🟢 | [Uruguay](https://www.gov.uk/foreign-travel-advice/uruguay) | No specific alerts |
| 🔴 | [Venezuela](https://www.gov.uk/foreign-travel-advice/venezuela) | avoid_all_travel_to_parts |
| 🔴 | [Benin](https://www.gov.uk/foreign-travel-advice/benin) | avoid_all_travel_to_parts |
| 🔴 | [Cameroon](https://www.gov.uk/foreign-travel-advice/cameroon) | avoid_all_travel_to_parts |
| 🔴 | [Central African Republic](https://www.gov.uk/foreign-travel-advice/central-african-republic) | avoid_all_travel_to_parts |
| 🔴 | [Chad](https://www.gov.uk/foreign-travel-advice/chad) | avoid_all_travel_to_parts |
| 🔴 | [Congo](https://www.gov.uk/foreign-travel-advice/congo) | avoid_all_travel_to_parts |
| 🟢 | [Japan](https://www.gov.uk/foreign-travel-advice/japan) | No specific alerts |
| 🟢 | [Montserrat](https://www.gov.uk/foreign-travel-advice/montserrat) | No specific alerts |
| 🟢 | [Nicaragua](https://www.gov.uk/foreign-travel-advice/nicaragua) | No specific alerts |
| 🟢 | [St Kitts and Nevis](https://www.gov.uk/foreign-travel-advice/st-kitts-and-nevis) | No specific alerts |
| 🟢 | [St Lucia](https://www.gov.uk/foreign-travel-advice/st-lucia) | No specific alerts |
| 🟢 | [St Maarten](https://www.gov.uk/foreign-travel-advice/st-maarten) | No specific alerts |
| 🟢 | [St Martin and St Barthélemy](https://www.gov.uk/foreign-travel-advice/st-martin-and-st-barthelemy) | No specific alerts |
| 🟢 | [St Pierre & Miquelon](https://www.gov.uk/foreign-travel-advice/st-pierre-and-miquelon) | No specific alerts |
| 🟢 | [St Vincent and the Grenadines](https://www.gov.uk/foreign-travel-advice/st-vincent-and-the-grenadines) | No specific alerts |
| 🟢 | [Turks and Caicos Islands](https://www.gov.uk/foreign-travel-advice/turks-and-caicos-islands) | No specific alerts |
| 🟢 | [Samoa](https://www.gov.uk/foreign-travel-advice/samoa) | No specific alerts |
| 🟢 | [Palau](https://www.gov.uk/foreign-travel-advice/palau) | No specific alerts |
| 🟢 | [Tuvalu](https://www.gov.uk/foreign-travel-advice/tuvalu) | No specific alerts |
| 🟢 | [Uzbekistan](https://www.gov.uk/foreign-travel-advice/uzbekistan) | No specific alerts |
| 🟢 | [Bahrain](https://www.gov.uk/foreign-travel-advice/bahrain) | No specific alerts |
| 🔴 | [Algeria](https://www.gov.uk/foreign-travel-advice/algeria) | avoid_all_travel_to_parts |
| 🔴* | [Ukraine](https://www.gov.uk/foreign-travel-advice/ukraine) | avoid_all_travel_to_parts, avoid_all_but_essential_travel_to_parts |
| 🟢 | [Wallis and Futuna](https://www.gov.uk/foreign-travel-advice/wallis-and-futuna) | No specific alerts |
| 🟢 | [Andorra](https://www.gov.uk/foreign-travel-advice/andorra) | No specific alerts |
| 🔴 | [Armenia](https://www.gov.uk/foreign-travel-advice/armenia) | avoid_all_travel_to_parts |
| 🟢 | [Kuwait](https://www.gov.uk/foreign-travel-advice/kuwait) | No specific alerts |
| 🟢 | [Morocco](https://www.gov.uk/foreign-travel-advice/morocco) | No specific alerts |
| 🟢 | [Bosnia and Herzegovina](https://www.gov.uk/foreign-travel-advice/bosnia-and-herzegovina) | No specific alerts |
| 🔴 | [Western Sahara](https://www.gov.uk/foreign-travel-advice/western-sahara) | avoid_all_travel_to_parts |
| 🔴 | [Yemen](https://www.gov.uk/foreign-travel-advice/yemen) | avoid_all_travel_to_whole_country |
| 🟢 | [Anguilla](https://www.gov.uk/foreign-travel-advice/anguilla) | No specific alerts |
| 🟢 | [Antigua and Barbuda](https://www.gov.uk/foreign-travel-advice/antigua-and-barbuda) | No specific alerts |
| 🟢 | [Aruba](https://www.gov.uk/foreign-travel-advice/aruba) | No specific alerts |
| 🟢 | [Bahamas](https://www.gov.uk/foreign-travel-advice/bahamas) | No specific alerts |
| 🟢 | [Bermuda](https://www.gov.uk/foreign-travel-advice/bermuda) | No specific alerts |
| 🟢 | [British Virgin Islands](https://www.gov.uk/foreign-travel-advice/british-virgin-islands) | No specific alerts |
| 🟢 | [Gibraltar](https://www.gov.uk/foreign-travel-advice/gibraltar) | No specific alerts |
| 🟢 | [Cayman Islands](https://www.gov.uk/foreign-travel-advice/cayman-islands) | No specific alerts |
| 🟢 | [Costa Rica](https://www.gov.uk/foreign-travel-advice/costa-rica) | No specific alerts |
| 🟢 | [Curaçao](https://www.gov.uk/foreign-travel-advice/curacao) | No specific alerts |
| 🟢 | [Ireland](https://www.gov.uk/foreign-travel-advice/ireland) | No specific alerts |
| 🟢 | [El Salvador](https://www.gov.uk/foreign-travel-advice/el-salvador) | No specific alerts |
| 🟡 | [Kosovo](https://www.gov.uk/foreign-travel-advice/kosovo) | avoid_all_but_essential_travel_to_parts |
| 🟢 | [Guadeloupe](https://www.gov.uk/foreign-travel-advice/guadeloupe) | No specific alerts |
| 🟡 | [Guatemala](https://www.gov.uk/foreign-travel-advice/guatemala) | avoid_all_but_essential_travel_to_parts |
| 🔴 | [Haiti](https://www.gov.uk/foreign-travel-advice/haiti) | avoid_all_travel_to_whole_country |
| 🟢 | [Honduras](https://www.gov.uk/foreign-travel-advice/honduras) | No specific alerts |
| 🟢 | [Jamaica](https://www.gov.uk/foreign-travel-advice/jamaica) | No specific alerts |
| 🟢 | [Martinique](https://www.gov.uk/foreign-travel-advice/martinique) | No specific alerts |
| 🟡 | [Mayotte](https://www.gov.uk/foreign-travel-advice/mayotte) | avoid_all_but_essential_travel_to_whole_country |
| 🟢 | [São Tomé and Principe](https://www.gov.uk/foreign-travel-advice/sao-tome-and-principe) | No specific alerts |
| 🔴 | [Moldova](https://www.gov.uk/foreign-travel-advice/moldova) | avoid_all_travel_to_parts |
| 🟢 | [Monaco](https://www.gov.uk/foreign-travel-advice/monaco) | No specific alerts |
| 🟢 | [Montenegro](https://www.gov.uk/foreign-travel-advice/montenegro) | No specific alerts |
| 🟢 | [Senegal](https://www.gov.uk/foreign-travel-advice/senegal) | No specific alerts |
| 🟢 | [North Macedonia](https://www.gov.uk/foreign-travel-advice/north-macedonia) | No specific alerts |
| 🔴 | [Tunisia](https://www.gov.uk/foreign-travel-advice/tunisia) | avoid_all_travel_to_parts |
| 🟡 | [Uganda](https://www.gov.uk/foreign-travel-advice/uganda) | avoid_all_but_essential_travel_to_parts |
| 🔴 | [Russia](https://www.gov.uk/foreign-travel-advice/russia) | avoid_all_travel_to_whole_country |
| 🟢 | [Bonaire/St Eustatius/Saba](https://www.gov.uk/foreign-travel-advice/bonaire-st-eustatius-saba) | No specific alerts |
| 🟢 | [San Marino](https://www.gov.uk/foreign-travel-advice/san-marino) | No specific alerts |
| 🟢 | [Liberia](https://www.gov.uk/foreign-travel-advice/liberia) | No specific alerts |
| 🔴 | [Mali](https://www.gov.uk/foreign-travel-advice/mali) | avoid_all_travel_to_parts |
| 🟢 | [Malawi](https://www.gov.uk/foreign-travel-advice/malawi) | No specific alerts |
| 🔴 | [Niger](https://www.gov.uk/foreign-travel-advice/niger) | avoid_all_travel_to_parts |
| 🟢 | [Cape Verde](https://www.gov.uk/foreign-travel-advice/cape-verde) | No specific alerts |
| 🟢 | [Canada](https://www.gov.uk/foreign-travel-advice/canada) | No specific alerts |
| 🟢 | [Vanuatu](https://www.gov.uk/foreign-travel-advice/vanuatu) | No specific alerts |
| 🟢 | [Chile](https://www.gov.uk/foreign-travel-advice/chile) | No specific alerts |
| 🟢 | [Falkland Islands](https://www.gov.uk/foreign-travel-advice/falkland-islands) | No specific alerts |
| 🔴 | [Jordan](https://www.gov.uk/foreign-travel-advice/jordan) | avoid_all_travel_to_parts |
| 🟢 | [Réunion](https://www.gov.uk/foreign-travel-advice/reunion) | No specific alerts |
| 🔴* | [Mozambique](https://www.gov.uk/foreign-travel-advice/mozambique) | avoid_all_travel_to_parts, avoid_all_but_essential_travel_to_parts |
| 🔴 | [Djibouti](https://www.gov.uk/foreign-travel-advice/djibouti) | avoid_all_travel_to_parts |
| 🔴 | [Iran](https://www.gov.uk/foreign-travel-advice/iran) | avoid_all_travel_to_whole_country |
| 🔴* | [Iraq](https://www.gov.uk/foreign-travel-advice/iraq) | avoid_all_travel_to_parts, avoid_all_but_essential_travel_to_parts |
| 🔴 | [Syria](https://www.gov.uk/foreign-travel-advice/syria) | avoid_all_travel_to_whole_country |
| 🔴* | [Ethiopia](https://www.gov.uk/foreign-travel-advice/ethiopia) | avoid_all_travel_to_parts, avoid_all_but_essential_travel_to_parts |
| 🟢 | [Guinea](https://www.gov.uk/foreign-travel-advice/guinea) | No specific alerts |
| 🟢 | [Cuba](https://www.gov.uk/foreign-travel-advice/cuba) | No specific alerts |
| 🟢 | [Maldives](https://www.gov.uk/foreign-travel-advice/maldives) | No specific alerts |
| 🟢 | [Argentina](https://www.gov.uk/foreign-travel-advice/argentina) | No specific alerts |
| 🔴 | [Israel](https://www.gov.uk/foreign-travel-advice/israel) | avoid_all_travel_to_parts |
| 🔴 | [The Occupied Palestinian Territories](https://www.gov.uk/foreign-travel-advice/the-occupied-palestinian-territories) | avoid_all_travel_to_parts |
| 🟡 | [Bolivia](https://www.gov.uk/foreign-travel-advice/bolivia) | avoid_all_but_essential_travel_to_parts |
| 🔴 | [Somalia](https://www.gov.uk/foreign-travel-advice/somalia) | avoid_all_travel_to_parts |
| 🟢 | [Nepal](https://www.gov.uk/foreign-travel-advice/nepal) | No specific alerts |

<!-- FCDO_TABLE_END -->

---

*Last updated: Automatically updated daily.*
