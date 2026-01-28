# FCDO Travel Advice Status Monitor

This repository contains a Python script that automatically fetches and monitors travel advice from the UK Foreign, Commonwealth & Development Office (FCDO) API. The script generates a comprehensive table showing the current travel advisory status for all countries worldwide.

## 🚦 Status Legend

The script uses a traffic light system to categorize travel advice:

- 🔴 **Red**: FCDO advises against all travel to the whole country
- ⚠️ **Warning**: FCDO advises against all travel to parts of the country
- 🟡 **Yellow**: FCDO advises against all but essential travel
- 🟢 **Green**: No specific travel advisories currently active
- ❓ **Unknown**: Error or unrecognized alert status

## 📊 Current Travel Advice Status

The table below is automatically updated daily at 2 AM UTC via GitHub Actions:

<!-- FCDO_TABLE_START -->
| Status | Country | FCDO Advice |
|:------:|---------|-------------|
| 🔴 | [Afghanistan](https://www.gov.uk/foreign-travel-advice/afghanistan) | FCDO advises against all travel to Afghanistan. |
| 🟢 | [Albania](https://www.gov.uk/foreign-travel-advice/albania) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Algeria](https://www.gov.uk/foreign-travel-advice/algeria) | FCDO advises against all travel to parts of Algeria. |
| 🟢 | [Andorra](https://www.gov.uk/foreign-travel-advice/andorra) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Angola](https://www.gov.uk/foreign-travel-advice/angola) | FCDO advises against all but essential travel to parts of Angola. |
| 🟢 | [Anguilla](https://www.gov.uk/foreign-travel-advice/anguilla) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Antarctica/British Antarctic Territory](https://www.gov.uk/foreign-travel-advice/antarctica-british-antarctic-territory) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Antigua and Barbuda](https://www.gov.uk/foreign-travel-advice/antigua-and-barbuda) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Argentina](https://www.gov.uk/foreign-travel-advice/argentina) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Armenia](https://www.gov.uk/foreign-travel-advice/armenia) | FCDO advises against all travel to parts of Armenia. |
| 🟢 | [Aruba](https://www.gov.uk/foreign-travel-advice/aruba) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Australia](https://www.gov.uk/foreign-travel-advice/australia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Austria](https://www.gov.uk/foreign-travel-advice/austria) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Azerbaijan](https://www.gov.uk/foreign-travel-advice/azerbaijan) | FCDO advises against all travel to parts of Azerbaijan.<br />FCDO advises against all but essential travel to parts of Azerbaijan. |
| 🟢 | [Bahamas](https://www.gov.uk/foreign-travel-advice/bahamas) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Bahrain](https://www.gov.uk/foreign-travel-advice/bahrain) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Bangladesh](https://www.gov.uk/foreign-travel-advice/bangladesh) | FCDO advises against all but essential travel to parts of Bangladesh. |
| 🟢 | [Barbados](https://www.gov.uk/foreign-travel-advice/barbados) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Belarus](https://www.gov.uk/foreign-travel-advice/belarus) | FCDO advises against all travel to Belarus. |
| 🟢 | [Belgium](https://www.gov.uk/foreign-travel-advice/belgium) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Belize](https://www.gov.uk/foreign-travel-advice/belize) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Benin](https://www.gov.uk/foreign-travel-advice/benin) | FCDO advises against all travel to parts of Benin.<br />FCDO advises against all but essential travel to parts of Benin. |
| 🟢 | [Bermuda](https://www.gov.uk/foreign-travel-advice/bermuda) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Bhutan](https://www.gov.uk/foreign-travel-advice/bhutan) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Bolivia](https://www.gov.uk/foreign-travel-advice/bolivia) | FCDO advises against all but essential travel to parts of Bolivia. |
| 🟢 | [Bonaire/St Eustatius/Saba](https://www.gov.uk/foreign-travel-advice/bonaire-st-eustatius-saba) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Bosnia and Herzegovina](https://www.gov.uk/foreign-travel-advice/bosnia-and-herzegovina) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Botswana](https://www.gov.uk/foreign-travel-advice/botswana) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Brazil](https://www.gov.uk/foreign-travel-advice/brazil) | FCDO advises against all but essential travel to parts of Brazil. |
| 🟢 | [British Indian Ocean Territory](https://www.gov.uk/foreign-travel-advice/british-indian-ocean-territory) | No specific FCDO travel advisories are currently active. |
| 🟢 | [British Virgin Islands](https://www.gov.uk/foreign-travel-advice/british-virgin-islands) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Brunei](https://www.gov.uk/foreign-travel-advice/brunei) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Bulgaria](https://www.gov.uk/foreign-travel-advice/bulgaria) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Burkina Faso](https://www.gov.uk/foreign-travel-advice/burkina-faso) | FCDO advises against all travel to Burkina Faso. |
| ⚠️ | [Burundi](https://www.gov.uk/foreign-travel-advice/burundi) | FCDO advises against all travel to parts of Burundi.<br />FCDO advises against all but essential travel to parts of Burundi. |
| ⚠️ | [Cambodia](https://www.gov.uk/foreign-travel-advice/cambodia) | FCDO advises against all travel to parts of Cambodia.<br />FCDO advises against all but essential travel to parts of Cambodia. |
| ⚠️ | [Cameroon](https://www.gov.uk/foreign-travel-advice/cameroon) | FCDO advises against all travel to parts of Cameroon. |
| 🟢 | [Canada](https://www.gov.uk/foreign-travel-advice/canada) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Cape Verde](https://www.gov.uk/foreign-travel-advice/cape-verde) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Cayman Islands](https://www.gov.uk/foreign-travel-advice/cayman-islands) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Central African Republic](https://www.gov.uk/foreign-travel-advice/central-african-republic) | FCDO advises against all travel to parts of Central African Republic. |
| ⚠️ | [Chad](https://www.gov.uk/foreign-travel-advice/chad) | FCDO advises against all travel to parts of Chad. |
| 🟢 | [Chile](https://www.gov.uk/foreign-travel-advice/chile) | No specific FCDO travel advisories are currently active. |
| 🟢 | [China](https://www.gov.uk/foreign-travel-advice/china) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Colombia](https://www.gov.uk/foreign-travel-advice/colombia) | FCDO advises against all but essential travel to parts of Colombia. |
| 🟢 | [Comoros](https://www.gov.uk/foreign-travel-advice/comoros) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Congo](https://www.gov.uk/foreign-travel-advice/congo) | FCDO advises against all travel to parts of Congo. |
| 🟢 | [Cook Islands, Tokelau and Niue](https://www.gov.uk/foreign-travel-advice/cook-islands-tokelau-and-niue) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Costa Rica](https://www.gov.uk/foreign-travel-advice/costa-rica) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Croatia](https://www.gov.uk/foreign-travel-advice/croatia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Cuba](https://www.gov.uk/foreign-travel-advice/cuba) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Curaçao](https://www.gov.uk/foreign-travel-advice/curacao) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Cyprus](https://www.gov.uk/foreign-travel-advice/cyprus) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Czechia](https://www.gov.uk/foreign-travel-advice/czechia) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Côte d'Ivoire](https://www.gov.uk/foreign-travel-advice/cote-d-ivoire) | FCDO advises against all travel to parts of Côte d'Ivoire. |
| ⚠️ | [Democratic Republic of the Congo](https://www.gov.uk/foreign-travel-advice/democratic-republic-of-the-congo) | FCDO advises against all travel to parts of Democratic Republic of the Congo. |
| 🟢 | [Denmark](https://www.gov.uk/foreign-travel-advice/denmark) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Djibouti](https://www.gov.uk/foreign-travel-advice/djibouti) | FCDO advises against all travel to parts of Djibouti. |
| 🟢 | [Dominica](https://www.gov.uk/foreign-travel-advice/dominica) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Dominican Republic](https://www.gov.uk/foreign-travel-advice/dominican-republic) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Ecuador](https://www.gov.uk/foreign-travel-advice/ecuador) | FCDO advises against all but essential travel to parts of Ecuador. |
| ⚠️ | [Egypt](https://www.gov.uk/foreign-travel-advice/egypt) | FCDO advises against all travel to parts of Egypt.<br />FCDO advises against all but essential travel to parts of Egypt. |
| 🟢 | [El Salvador](https://www.gov.uk/foreign-travel-advice/el-salvador) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Equatorial Guinea](https://www.gov.uk/foreign-travel-advice/equatorial-guinea) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Eritrea](https://www.gov.uk/foreign-travel-advice/eritrea) | FCDO advises against all travel to parts of Eritrea. |
| 🟢 | [Estonia](https://www.gov.uk/foreign-travel-advice/estonia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Eswatini](https://www.gov.uk/foreign-travel-advice/eswatini) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Ethiopia](https://www.gov.uk/foreign-travel-advice/ethiopia) | FCDO advises against all travel to parts of Ethiopia.<br />FCDO advises against all but essential travel to parts of Ethiopia. |
| 🟢 | [Falkland Islands](https://www.gov.uk/foreign-travel-advice/falkland-islands) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Federated States of Micronesia](https://www.gov.uk/foreign-travel-advice/federated-states-of-micronesia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Fiji](https://www.gov.uk/foreign-travel-advice/fiji) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Finland](https://www.gov.uk/foreign-travel-advice/finland) | No specific FCDO travel advisories are currently active. |
| 🟢 | [France](https://www.gov.uk/foreign-travel-advice/france) | No specific FCDO travel advisories are currently active. |
| 🟢 | [French Guiana](https://www.gov.uk/foreign-travel-advice/french-guiana) | No specific FCDO travel advisories are currently active. |
| 🟢 | [French Polynesia](https://www.gov.uk/foreign-travel-advice/french-polynesia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Gabon](https://www.gov.uk/foreign-travel-advice/gabon) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Georgia](https://www.gov.uk/foreign-travel-advice/georgia) | FCDO advises against all travel to parts of Georgia. |
| 🟢 | [Germany](https://www.gov.uk/foreign-travel-advice/germany) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Ghana](https://www.gov.uk/foreign-travel-advice/ghana) | FCDO advises against all but essential travel to parts of Ghana. |
| 🟢 | [Gibraltar](https://www.gov.uk/foreign-travel-advice/gibraltar) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Greece](https://www.gov.uk/foreign-travel-advice/greece) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Grenada](https://www.gov.uk/foreign-travel-advice/grenada) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Guadeloupe](https://www.gov.uk/foreign-travel-advice/guadeloupe) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Guatemala](https://www.gov.uk/foreign-travel-advice/guatemala) | FCDO advises against all but essential travel to parts of Guatemala. |
| 🟢 | [Guinea](https://www.gov.uk/foreign-travel-advice/guinea) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Guinea-Bissau](https://www.gov.uk/foreign-travel-advice/guinea-bissau) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Guyana](https://www.gov.uk/foreign-travel-advice/guyana) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Haiti](https://www.gov.uk/foreign-travel-advice/haiti) | FCDO advises against all travel to Haiti. |
| 🟢 | [Honduras](https://www.gov.uk/foreign-travel-advice/honduras) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Hong Kong](https://www.gov.uk/foreign-travel-advice/hong-kong) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Hungary](https://www.gov.uk/foreign-travel-advice/hungary) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Iceland](https://www.gov.uk/foreign-travel-advice/iceland) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [India](https://www.gov.uk/foreign-travel-advice/india) | FCDO advises against all travel to parts of India. |
| ⚠️ | [Indonesia](https://www.gov.uk/foreign-travel-advice/indonesia) | FCDO advises against all travel to parts of Indonesia. |
| 🔴 | [Iran](https://www.gov.uk/foreign-travel-advice/iran) | FCDO advises against all travel to Iran. |
| ⚠️ | [Iraq](https://www.gov.uk/foreign-travel-advice/iraq) | FCDO advises against all travel to parts of Iraq.<br />FCDO advises against all but essential travel to parts of Iraq. |
| 🟢 | [Ireland](https://www.gov.uk/foreign-travel-advice/ireland) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Israel](https://www.gov.uk/foreign-travel-advice/israel) | FCDO advises against all travel to parts of Israel.<br />FCDO advises against all but essential travel to parts of Israel. |
| 🟢 | [Italy](https://www.gov.uk/foreign-travel-advice/italy) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Jamaica](https://www.gov.uk/foreign-travel-advice/jamaica) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Japan](https://www.gov.uk/foreign-travel-advice/japan) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Jordan](https://www.gov.uk/foreign-travel-advice/jordan) | FCDO advises against all travel to parts of Jordan. |
| 🟢 | [Kazakhstan](https://www.gov.uk/foreign-travel-advice/kazakhstan) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Kenya](https://www.gov.uk/foreign-travel-advice/kenya) | FCDO advises against all travel to parts of Kenya.<br />FCDO advises against all but essential travel to parts of Kenya. |
| 🟢 | [Kiribati](https://www.gov.uk/foreign-travel-advice/kiribati) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Kosovo](https://www.gov.uk/foreign-travel-advice/kosovo) | FCDO advises against all but essential travel to parts of Kosovo. |
| 🟢 | [Kuwait](https://www.gov.uk/foreign-travel-advice/kuwait) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Kyrgyzstan](https://www.gov.uk/foreign-travel-advice/kyrgyzstan) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Laos](https://www.gov.uk/foreign-travel-advice/laos) | FCDO advises against all but essential travel to parts of Laos. |
| 🟢 | [Latvia](https://www.gov.uk/foreign-travel-advice/latvia) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Lebanon](https://www.gov.uk/foreign-travel-advice/lebanon) | FCDO advises against all travel to parts of Lebanon. |
| 🟢 | [Lesotho](https://www.gov.uk/foreign-travel-advice/lesotho) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Liberia](https://www.gov.uk/foreign-travel-advice/liberia) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Libya](https://www.gov.uk/foreign-travel-advice/libya) | FCDO advises against all travel to parts of Libya.<br />FCDO advises against all but essential travel to parts of Libya. |
| 🟢 | [Liechtenstein](https://www.gov.uk/foreign-travel-advice/liechtenstein) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Lithuania](https://www.gov.uk/foreign-travel-advice/lithuania) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Luxembourg](https://www.gov.uk/foreign-travel-advice/luxembourg) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Macao](https://www.gov.uk/foreign-travel-advice/macao) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Madagascar](https://www.gov.uk/foreign-travel-advice/madagascar) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Malawi](https://www.gov.uk/foreign-travel-advice/malawi) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Malaysia](https://www.gov.uk/foreign-travel-advice/malaysia) | FCDO advises against all but essential travel to parts of Malaysia. |
| 🟢 | [Maldives](https://www.gov.uk/foreign-travel-advice/maldives) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Mali](https://www.gov.uk/foreign-travel-advice/mali) | FCDO advises against all travel to Mali. |
| 🟢 | [Malta](https://www.gov.uk/foreign-travel-advice/malta) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Marshall Islands](https://www.gov.uk/foreign-travel-advice/marshall-islands) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Martinique](https://www.gov.uk/foreign-travel-advice/martinique) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Mauritania](https://www.gov.uk/foreign-travel-advice/mauritania) | FCDO advises against all travel to parts of Mauritania. |
| 🟢 | [Mauritius](https://www.gov.uk/foreign-travel-advice/mauritius) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Mayotte](https://www.gov.uk/foreign-travel-advice/mayotte) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Mexico](https://www.gov.uk/foreign-travel-advice/mexico) | FCDO advises against all but essential travel to parts of Mexico. |
| ⚠️ | [Moldova](https://www.gov.uk/foreign-travel-advice/moldova) | FCDO advises against all travel to parts of Moldova. |
| 🟢 | [Monaco](https://www.gov.uk/foreign-travel-advice/monaco) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Mongolia](https://www.gov.uk/foreign-travel-advice/mongolia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Montenegro](https://www.gov.uk/foreign-travel-advice/montenegro) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Montserrat](https://www.gov.uk/foreign-travel-advice/montserrat) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Morocco](https://www.gov.uk/foreign-travel-advice/morocco) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Mozambique](https://www.gov.uk/foreign-travel-advice/mozambique) | FCDO advises against all travel to parts of Mozambique.<br />FCDO advises against all but essential travel to parts of Mozambique. |
| ⚠️ | [Myanmar (Burma)](https://www.gov.uk/foreign-travel-advice/myanmar) | FCDO advises against all travel to parts of Myanmar (Burma).<br />FCDO advises against all but essential travel to parts of Myanmar (Burma). |
| 🟢 | [Namibia](https://www.gov.uk/foreign-travel-advice/namibia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Nauru](https://www.gov.uk/foreign-travel-advice/nauru) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Nepal](https://www.gov.uk/foreign-travel-advice/nepal) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Netherlands](https://www.gov.uk/foreign-travel-advice/netherlands) | No specific FCDO travel advisories are currently active. |
| 🟢 | [New Caledonia](https://www.gov.uk/foreign-travel-advice/new-caledonia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [New Zealand](https://www.gov.uk/foreign-travel-advice/new-zealand) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Nicaragua](https://www.gov.uk/foreign-travel-advice/nicaragua) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Niger](https://www.gov.uk/foreign-travel-advice/niger) | FCDO advises against all travel to Niger. |
| ⚠️ | [Nigeria](https://www.gov.uk/foreign-travel-advice/nigeria) | FCDO advises against all travel to parts of Nigeria. |
| 🟡 | [North Korea](https://www.gov.uk/foreign-travel-advice/north-korea) | FCDO advises against all but essential travel to North Korea. |
| 🟢 | [North Macedonia](https://www.gov.uk/foreign-travel-advice/north-macedonia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Norway](https://www.gov.uk/foreign-travel-advice/norway) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Oman](https://www.gov.uk/foreign-travel-advice/oman) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Pakistan](https://www.gov.uk/foreign-travel-advice/pakistan) | FCDO advises against all travel to parts of Pakistan.<br />FCDO advises against all but essential travel to parts of Pakistan. |
| 🟢 | [Palau](https://www.gov.uk/foreign-travel-advice/palau) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Palestine](https://www.gov.uk/foreign-travel-advice/palestine) | FCDO advises against all travel to parts of Palestine.<br />FCDO advises against all but essential travel to parts of Palestine. |
| 🟢 | [Panama](https://www.gov.uk/foreign-travel-advice/panama) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Papua New Guinea](https://www.gov.uk/foreign-travel-advice/papua-new-guinea) | FCDO advises against all but essential travel to parts of Papua New Guinea. |
| 🟢 | [Paraguay](https://www.gov.uk/foreign-travel-advice/paraguay) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Peru](https://www.gov.uk/foreign-travel-advice/peru) | FCDO advises against all but essential travel to parts of Peru. |
| ⚠️ | [Philippines](https://www.gov.uk/foreign-travel-advice/philippines) | FCDO advises against all travel to parts of Philippines. |
| 🟢 | [Pitcairn Island](https://www.gov.uk/foreign-travel-advice/pitcairn-island) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Poland](https://www.gov.uk/foreign-travel-advice/poland) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Portugal](https://www.gov.uk/foreign-travel-advice/portugal) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Qatar](https://www.gov.uk/foreign-travel-advice/qatar) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Romania](https://www.gov.uk/foreign-travel-advice/romania) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Russia](https://www.gov.uk/foreign-travel-advice/russia) | FCDO advises against all travel to Russia. |
| 🟡 | [Rwanda](https://www.gov.uk/foreign-travel-advice/rwanda) | FCDO advises against all but essential travel to parts of Rwanda. |
| 🟢 | [Réunion](https://www.gov.uk/foreign-travel-advice/reunion) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Samoa](https://www.gov.uk/foreign-travel-advice/samoa) | No specific FCDO travel advisories are currently active. |
| 🟢 | [San Marino](https://www.gov.uk/foreign-travel-advice/san-marino) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Saudi Arabia](https://www.gov.uk/foreign-travel-advice/saudi-arabia) | FCDO advises against all travel to parts of Saudi Arabia. |
| 🟢 | [Senegal](https://www.gov.uk/foreign-travel-advice/senegal) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Serbia](https://www.gov.uk/foreign-travel-advice/serbia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Seychelles](https://www.gov.uk/foreign-travel-advice/seychelles) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Sierra Leone](https://www.gov.uk/foreign-travel-advice/sierra-leone) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Singapore](https://www.gov.uk/foreign-travel-advice/singapore) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Slovakia](https://www.gov.uk/foreign-travel-advice/slovakia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Slovenia](https://www.gov.uk/foreign-travel-advice/slovenia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Solomon Islands](https://www.gov.uk/foreign-travel-advice/solomon-islands) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Somalia](https://www.gov.uk/foreign-travel-advice/somalia) | FCDO advises against all travel to parts of Somalia. |
| 🟢 | [South Africa](https://www.gov.uk/foreign-travel-advice/south-africa) | No specific FCDO travel advisories are currently active. |
| 🟢 | [South Georgia and the South Sandwich Islands](https://www.gov.uk/foreign-travel-advice/south-georgia-and-south-sandwich-islands) | No specific FCDO travel advisories are currently active. |
| 🟢 | [South Korea](https://www.gov.uk/foreign-travel-advice/south-korea) | No specific FCDO travel advisories are currently active. |
| 🔴 | [South Sudan](https://www.gov.uk/foreign-travel-advice/south-sudan) | FCDO advises against all travel to South Sudan. |
| 🟢 | [Spain](https://www.gov.uk/foreign-travel-advice/spain) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Sri Lanka](https://www.gov.uk/foreign-travel-advice/sri-lanka) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Helena, Ascension and Tristan da Cunha](https://www.gov.uk/foreign-travel-advice/st-helena-ascension-and-tristan-da-cunha) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Kitts and Nevis](https://www.gov.uk/foreign-travel-advice/st-kitts-and-nevis) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Lucia](https://www.gov.uk/foreign-travel-advice/st-lucia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Maarten](https://www.gov.uk/foreign-travel-advice/st-maarten) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Martin and St Barthélemy](https://www.gov.uk/foreign-travel-advice/st-martin-and-st-barthelemy) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Pierre & Miquelon](https://www.gov.uk/foreign-travel-advice/st-pierre-and-miquelon) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Vincent and the Grenadines](https://www.gov.uk/foreign-travel-advice/st-vincent-and-the-grenadines) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Sudan](https://www.gov.uk/foreign-travel-advice/sudan) | FCDO advises against all travel to parts of Sudan. |
| 🟢 | [Suriname](https://www.gov.uk/foreign-travel-advice/suriname) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Sweden](https://www.gov.uk/foreign-travel-advice/sweden) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Switzerland](https://www.gov.uk/foreign-travel-advice/switzerland) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Syria](https://www.gov.uk/foreign-travel-advice/syria) | FCDO advises against all travel to Syria. |
| 🟢 | [São Tomé and Principe](https://www.gov.uk/foreign-travel-advice/sao-tome-and-principe) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Taiwan](https://www.gov.uk/foreign-travel-advice/taiwan) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Tajikistan](https://www.gov.uk/foreign-travel-advice/tajikistan) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Tanzania](https://www.gov.uk/foreign-travel-advice/tanzania) | FCDO advises against all but essential travel to parts of Tanzania. |
| ⚠️ | [Thailand](https://www.gov.uk/foreign-travel-advice/thailand) | FCDO advises against all travel to parts of Thailand.<br />FCDO advises against all but essential travel to parts of Thailand. |
| 🟢 | [The Gambia](https://www.gov.uk/foreign-travel-advice/the-gambia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Timor-Leste](https://www.gov.uk/foreign-travel-advice/timor-leste) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Togo](https://www.gov.uk/foreign-travel-advice/togo) | FCDO advises against all travel to parts of Togo.<br />FCDO advises against all but essential travel to parts of Togo. |
| 🟢 | [Tonga](https://www.gov.uk/foreign-travel-advice/tonga) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Trinidad and Tobago](https://www.gov.uk/foreign-travel-advice/trinidad-and-tobago) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Tunisia](https://www.gov.uk/foreign-travel-advice/tunisia) | FCDO advises against all travel to parts of Tunisia. |
| ⚠️ | [Turkey](https://www.gov.uk/foreign-travel-advice/turkey) | FCDO advises against all travel to parts of Turkey. |
| 🟢 | [Turkmenistan](https://www.gov.uk/foreign-travel-advice/turkmenistan) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Turks and Caicos Islands](https://www.gov.uk/foreign-travel-advice/turks-and-caicos-islands) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Tuvalu](https://www.gov.uk/foreign-travel-advice/tuvalu) | No specific FCDO travel advisories are currently active. |
| 🟢 | [USA](https://www.gov.uk/foreign-travel-advice/usa) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Uganda](https://www.gov.uk/foreign-travel-advice/uganda) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Ukraine](https://www.gov.uk/foreign-travel-advice/ukraine) | FCDO advises against all travel to parts of Ukraine.<br />FCDO advises against all but essential travel to parts of Ukraine. |
| 🟢 | [United Arab Emirates](https://www.gov.uk/foreign-travel-advice/united-arab-emirates) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Uruguay](https://www.gov.uk/foreign-travel-advice/uruguay) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Uzbekistan](https://www.gov.uk/foreign-travel-advice/uzbekistan) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Vanuatu](https://www.gov.uk/foreign-travel-advice/vanuatu) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Venezuela](https://www.gov.uk/foreign-travel-advice/venezuela) | FCDO advises against all travel to Venezuela. |
| 🟢 | [Vietnam](https://www.gov.uk/foreign-travel-advice/vietnam) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Wallis and Futuna](https://www.gov.uk/foreign-travel-advice/wallis-and-futuna) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Western Sahara](https://www.gov.uk/foreign-travel-advice/western-sahara) | FCDO advises against all travel to parts of Western Sahara. |
| 🔴 | [Yemen](https://www.gov.uk/foreign-travel-advice/yemen) | FCDO advises against all travel to Yemen. |
| 🟢 | [Zambia](https://www.gov.uk/foreign-travel-advice/zambia) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Zimbabwe](https://www.gov.uk/foreign-travel-advice/zimbabwe) | No specific FCDO travel advisories are currently active. |

<!-- FCDO_TABLE_END -->

*Last updated: 2026-01-28 02:52 UTC*

## 🛠️ Usage

### Prerequisites

- Python 3.7 or higher
- Internet connection for API access

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/fcdo-travel-advice.git
   cd fcdo-travel-advice
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Script

#### Basic Usage
```bash
# Output to console
python get_status.py

# Output to file
python get_status.py -o travel_advice.md
```

#### Test Mode
```bash
# Run with a small subset of countries for testing
python get_status.py --test
```

#### Command Line Options
```bash
python get_status.py --help
```

- `--test`: Run in test mode with predefined countries
- `-o, --output FILE`: Specify output file path
- `--version`: Show version information

## 🤖 Automation

This repository includes GitHub Actions workflows for automation:

### Daily Updates (`update_readme.yml`)
- Runs daily at 2 AM UTC
- Fetches latest travel advice data
- Updates the table in this README automatically
- Commits changes back to the repository

### Manual Testing (`test_run.yml`)
- Can be triggered manually from the Actions tab
- Runs the script in test mode for verification
- Useful for testing changes without affecting the main table

## 📁 Project Structure

```
fcdo-travel-advice/
├── .github/workflows/     # GitHub Actions workflows
│   ├── update_readme.yml  # Daily automated updates
│   └── test_run.yml       # Manual testing workflow
├── get_status.py          # Main Python script
├── requirements.txt       # Python dependencies
├── LICENSE               # MIT License
├── README.md             # This file (auto-updated)
└── .gitignore           # Git ignore rules
```

## 🔧 Technical Details

### Data Source
The script fetches data from the official FCDO API:
- Base URL: `https://www.gov.uk/api/content/foreign-travel-advice`
- Real-time data directly from government sources
- Comprehensive coverage of all countries and territories

### Processing Logic
1. Fetches the complete list of countries from the API
2. Retrieves detailed travel advice for each country
3. Categorizes advice using the traffic light system
4. Generates a sorted Markdown table
5. Handles errors gracefully with appropriate status indicators

### Error Handling
- Network timeouts and connection errors
- Invalid or missing API data
- Unrecognized alert statuses
- Comprehensive logging to stderr

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## ⚠️ Disclaimer

This tool is for informational purposes only. Always check the official FCDO website at [gov.uk/foreign-travel-advice](https://www.gov.uk/foreign-travel-advice) for the most current and detailed travel advice before making travel decisions.

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](../../issues) page for existing problems
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about the error and your environment
