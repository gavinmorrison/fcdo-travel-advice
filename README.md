# FCDO Travel Advice Status Monitor

This repository contains a Python script that automatically fetches and monitors travel advice from the UK Foreign, Commonwealth & Development Office (FCDO) API. The script generates a comprehensive table showing the current travel advisory status for all countries worldwide.

> [!NOTE]
> Country and territory names, groupings, and designations are sourced directly from the UK government's FCDO API and do not represent the views or opinions of the author.

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
| 🔴 | [Afghanistan](countries/afghanistan.md) | FCDO advises against all travel to Afghanistan. |
| 🟢 | [Albania](countries/albania.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Algeria](countries/algeria.md) | FCDO advises against all travel to parts of Algeria. |
| 🟢 | [Andorra](countries/andorra.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Angola](countries/angola.md) | FCDO advises against all but essential travel to parts of Angola. |
| 🟢 | [Anguilla](countries/anguilla.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Antarctica/British Antarctic Territory](countries/antarctica-british-antarctic-territory.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Antigua and Barbuda](countries/antigua-and-barbuda.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Argentina](countries/argentina.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Armenia](countries/armenia.md) | FCDO advises against all travel to parts of Armenia. |
| 🟢 | [Aruba](countries/aruba.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Australia](countries/australia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Austria](countries/austria.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Azerbaijan](countries/azerbaijan.md) | FCDO advises against all travel to parts of Azerbaijan.<br />FCDO advises against all but essential travel to parts of Azerbaijan. |
| 🟢 | [Bahamas](countries/bahamas.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Bahrain](countries/bahrain.md) | FCDO advises against all but essential travel to Bahrain. |
| 🟡 | [Bangladesh](countries/bangladesh.md) | FCDO advises against all but essential travel to parts of Bangladesh. |
| 🟢 | [Barbados](countries/barbados.md) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Belarus](countries/belarus.md) | FCDO advises against all travel to Belarus. |
| 🟢 | [Belgium](countries/belgium.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Belize](countries/belize.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Benin](countries/benin.md) | FCDO advises against all travel to parts of Benin.<br />FCDO advises against all but essential travel to parts of Benin. |
| 🟢 | [Bermuda](countries/bermuda.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Bhutan](countries/bhutan.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Bolivia](countries/bolivia.md) | FCDO advises against all but essential travel to parts of Bolivia. |
| 🟢 | [Bonaire/St Eustatius/Saba](countries/bonaire-st-eustatius-saba.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Bosnia and Herzegovina](countries/bosnia-and-herzegovina.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Botswana](countries/botswana.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Brazil](countries/brazil.md) | FCDO advises against all but essential travel to parts of Brazil. |
| 🟢 | [British Indian Ocean Territory](countries/british-indian-ocean-territory.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [British Virgin Islands](countries/british-virgin-islands.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Brunei](countries/brunei.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Bulgaria](countries/bulgaria.md) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Burkina Faso](countries/burkina-faso.md) | FCDO advises against all travel to Burkina Faso. |
| ⚠️ | [Burundi](countries/burundi.md) | FCDO advises against all travel to parts of Burundi. |
| 🟡 | [Cambodia](countries/cambodia.md) | FCDO advises against all but essential travel to parts of Cambodia. |
| ⚠️ | [Cameroon](countries/cameroon.md) | FCDO advises against all travel to parts of Cameroon.<br />FCDO advises against all but essential travel to parts of Cameroon. |
| 🟢 | [Canada](countries/canada.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Cape Verde](countries/cape-verde.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Cayman Islands](countries/cayman-islands.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Central African Republic](countries/central-african-republic.md) | FCDO advises against all travel to parts of Central African Republic. |
| ⚠️ | [Chad](countries/chad.md) | FCDO advises against all travel to parts of Chad. |
| 🟢 | [Chile](countries/chile.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [China](countries/china.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Colombia](countries/colombia.md) | FCDO advises against all but essential travel to parts of Colombia. |
| 🟢 | [Comoros](countries/comoros.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Congo](countries/congo.md) | FCDO advises against all travel to parts of Congo. |
| 🟢 | [Cook Islands, Tokelau and Niue](countries/cook-islands-tokelau-and-niue.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Costa Rica](countries/costa-rica.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Croatia](countries/croatia.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Cuba](countries/cuba.md) | FCDO advises against all but essential travel to Cuba. |
| 🟢 | [Curaçao](countries/curacao.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Cyprus](countries/cyprus.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Czechia](countries/czechia.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Côte d'Ivoire](countries/cote-d-ivoire.md) | FCDO advises against all travel to parts of Côte d'Ivoire. |
| ⚠️ | [Democratic Republic of the Congo](countries/democratic-republic-of-the-congo.md) | FCDO advises against all travel to parts of Democratic Republic of the Congo.<br />FCDO advises against all but essential travel to parts of Democratic Republic of the Congo. |
| 🟢 | [Denmark](countries/denmark.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Djibouti](countries/djibouti.md) | FCDO advises against all travel to parts of Djibouti. |
| 🟢 | [Dominica](countries/dominica.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Dominican Republic](countries/dominican-republic.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Ecuador](countries/ecuador.md) | FCDO advises against all but essential travel to parts of Ecuador. |
| ⚠️ | [Egypt](countries/egypt.md) | FCDO advises against all travel to parts of Egypt.<br />FCDO advises against all but essential travel to parts of Egypt. |
| 🟢 | [El Salvador](countries/el-salvador.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Equatorial Guinea](countries/equatorial-guinea.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Eritrea](countries/eritrea.md) | FCDO advises against all travel to parts of Eritrea. |
| 🟢 | [Estonia](countries/estonia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Eswatini](countries/eswatini.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Ethiopia](countries/ethiopia.md) | FCDO advises against all travel to parts of Ethiopia.<br />FCDO advises against all but essential travel to parts of Ethiopia. |
| 🟢 | [Falkland Islands](countries/falkland-islands.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Federated States of Micronesia](countries/federated-states-of-micronesia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Fiji](countries/fiji.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Finland](countries/finland.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [France](countries/france.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [French Guiana](countries/french-guiana.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [French Polynesia](countries/french-polynesia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Gabon](countries/gabon.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Georgia](countries/georgia.md) | FCDO advises against all travel to parts of Georgia. |
| 🟢 | [Germany](countries/germany.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Ghana](countries/ghana.md) | FCDO advises against all but essential travel to parts of Ghana. |
| 🟢 | [Gibraltar](countries/gibraltar.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Greece](countries/greece.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Grenada](countries/grenada.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Guadeloupe](countries/guadeloupe.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Guatemala](countries/guatemala.md) | FCDO advises against all but essential travel to parts of Guatemala. |
| 🟢 | [Guinea](countries/guinea.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Guinea-Bissau](countries/guinea-bissau.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Guyana](countries/guyana.md) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Haiti](countries/haiti.md) | FCDO advises against all travel to Haiti. |
| 🟢 | [Honduras](countries/honduras.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Hong Kong](countries/hong-kong.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Hungary](countries/hungary.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Iceland](countries/iceland.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [India](countries/india.md) | FCDO advises against all travel to parts of India. |
| ⚠️ | [Indonesia](countries/indonesia.md) | FCDO advises against all travel to parts of Indonesia. |
| 🔴 | [Iran](countries/iran.md) | FCDO advises against all travel to Iran. |
| 🔴 | [Iraq](countries/iraq.md) | FCDO advises against all travel to Iraq. |
| 🟢 | [Ireland](countries/ireland.md) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Israel](countries/israel.md) | FCDO advises against all travel to Israel. |
| 🟢 | [Italy](countries/italy.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Jamaica](countries/jamaica.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Japan](countries/japan.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Jordan](countries/jordan.md) | FCDO advises against all travel to parts of Jordan.<br />FCDO advises against all but essential travel to parts of Jordan. |
| 🟢 | [Kazakhstan](countries/kazakhstan.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Kenya](countries/kenya.md) | FCDO advises against all travel to parts of Kenya.<br />FCDO advises against all but essential travel to parts of Kenya. |
| 🟢 | [Kiribati](countries/kiribati.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Kosovo](countries/kosovo.md) | FCDO advises against all but essential travel to parts of Kosovo. |
| 🟡 | [Kuwait](countries/kuwait.md) | FCDO advises against all but essential travel to Kuwait. |
| 🟢 | [Kyrgyzstan](countries/kyrgyzstan.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Laos](countries/laos.md) | FCDO advises against all but essential travel to parts of Laos. |
| 🟢 | [Latvia](countries/latvia.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Lebanon](countries/lebanon.md) | FCDO advises against all travel to parts of Lebanon.<br />FCDO advises against all but essential travel to parts of Lebanon. |
| 🟢 | [Lesotho](countries/lesotho.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Liberia](countries/liberia.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Libya](countries/libya.md) | FCDO advises against all travel to parts of Libya.<br />FCDO advises against all but essential travel to parts of Libya. |
| 🟢 | [Liechtenstein](countries/liechtenstein.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Lithuania](countries/lithuania.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Luxembourg](countries/luxembourg.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Macao](countries/macao.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Madagascar](countries/madagascar.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Malawi](countries/malawi.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Malaysia](countries/malaysia.md) | FCDO advises against all but essential travel to parts of Malaysia. |
| 🟢 | [Maldives](countries/maldives.md) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Mali](countries/mali.md) | FCDO advises against all travel to Mali. |
| 🟢 | [Malta](countries/malta.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Marshall Islands](countries/marshall-islands.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Martinique](countries/martinique.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Mauritania](countries/mauritania.md) | FCDO advises against all travel to parts of Mauritania. |
| 🟢 | [Mauritius](countries/mauritius.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Mayotte](countries/mayotte.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Mexico](countries/mexico.md) | FCDO advises against all but essential travel to parts of Mexico. |
| ⚠️ | [Moldova](countries/moldova.md) | FCDO advises against all travel to parts of Moldova. |
| 🟢 | [Monaco](countries/monaco.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Mongolia](countries/mongolia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Montenegro](countries/montenegro.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Montserrat](countries/montserrat.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Morocco](countries/morocco.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Mozambique](countries/mozambique.md) | FCDO advises against all travel to parts of Mozambique.<br />FCDO advises against all but essential travel to parts of Mozambique. |
| ⚠️ | [Myanmar (Burma)](countries/myanmar.md) | FCDO advises against all travel to parts of Myanmar (Burma).<br />FCDO advises against all but essential travel to parts of Myanmar (Burma). |
| 🟢 | [Namibia](countries/namibia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Nauru](countries/nauru.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Nepal](countries/nepal.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Netherlands](countries/netherlands.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [New Caledonia](countries/new-caledonia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [New Zealand](countries/new-zealand.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Nicaragua](countries/nicaragua.md) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Niger](countries/niger.md) | FCDO advises against all travel to Niger. |
| ⚠️ | [Nigeria](countries/nigeria.md) | FCDO advises against all travel to parts of Nigeria. |
| 🟡 | [North Korea](countries/north-korea.md) | FCDO advises against all but essential travel to North Korea. |
| 🟢 | [North Macedonia](countries/north-macedonia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Norway](countries/norway.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Oman](countries/oman.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Pakistan](countries/pakistan.md) | FCDO advises against all travel to parts of Pakistan.<br />FCDO advises against all but essential travel to parts of Pakistan. |
| 🟢 | [Palau](countries/palau.md) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Palestine](countries/palestine.md) | FCDO advises against all travel to Palestine. |
| 🟢 | [Panama](countries/panama.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Papua New Guinea](countries/papua-new-guinea.md) | FCDO advises against all but essential travel to parts of Papua New Guinea. |
| 🟢 | [Paraguay](countries/paraguay.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Peru](countries/peru.md) | FCDO advises against all but essential travel to parts of Peru. |
| ⚠️ | [Philippines](countries/philippines.md) | FCDO advises against all travel to parts of Philippines. |
| 🟢 | [Pitcairn Island](countries/pitcairn-island.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Poland](countries/poland.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Portugal](countries/portugal.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Qatar](countries/qatar.md) | FCDO advises against all but essential travel to Qatar. |
| 🟢 | [Romania](countries/romania.md) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Russia](countries/russia.md) | FCDO advises against all travel to Russia. |
| 🟡 | [Rwanda](countries/rwanda.md) | FCDO advises against all but essential travel to parts of Rwanda. |
| 🟢 | [Réunion](countries/reunion.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Samoa](countries/samoa.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [San Marino](countries/san-marino.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Saudi Arabia](countries/saudi-arabia.md) | FCDO advises against all travel to parts of Saudi Arabia.<br />FCDO advises against all but essential travel to parts of Saudi Arabia. |
| 🟢 | [Senegal](countries/senegal.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Serbia](countries/serbia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Seychelles](countries/seychelles.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Sierra Leone](countries/sierra-leone.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Singapore](countries/singapore.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Slovakia](countries/slovakia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Slovenia](countries/slovenia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Solomon Islands](countries/solomon-islands.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Somalia](countries/somalia.md) | FCDO advises against all travel to parts of Somalia. |
| 🟢 | [South Africa](countries/south-africa.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [South Georgia and the South Sandwich Islands](countries/south-georgia-and-south-sandwich-islands.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [South Korea](countries/south-korea.md) | No specific FCDO travel advisories are currently active. |
| 🔴 | [South Sudan](countries/south-sudan.md) | FCDO advises against all travel to South Sudan. |
| 🟢 | [Spain](countries/spain.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Sri Lanka](countries/sri-lanka.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Helena, Ascension and Tristan da Cunha](countries/st-helena-ascension-and-tristan-da-cunha.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Kitts and Nevis](countries/st-kitts-and-nevis.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Lucia](countries/st-lucia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Maarten](countries/st-maarten.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Martin and St Barthélemy](countries/st-martin-and-st-barthelemy.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Pierre & Miquelon](countries/st-pierre-and-miquelon.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [St Vincent and the Grenadines](countries/st-vincent-and-the-grenadines.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Sudan](countries/sudan.md) | FCDO advises against all travel to parts of Sudan. |
| 🟢 | [Suriname](countries/suriname.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Sweden](countries/sweden.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Switzerland](countries/switzerland.md) | No specific FCDO travel advisories are currently active. |
| 🔴 | [Syria](countries/syria.md) | FCDO advises against all travel to Syria. |
| 🟢 | [São Tomé and Principe](countries/sao-tome-and-principe.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Taiwan](countries/taiwan.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Tajikistan](countries/tajikistan.md) | No specific FCDO travel advisories are currently active. |
| 🟡 | [Tanzania](countries/tanzania.md) | FCDO advises against all but essential travel to parts of Tanzania. |
| 🟡 | [Thailand](countries/thailand.md) | FCDO advises against all but essential travel to parts of Thailand. |
| 🟢 | [The Gambia](countries/the-gambia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Timor-Leste](countries/timor-leste.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Togo](countries/togo.md) | FCDO advises against all travel to parts of Togo.<br />FCDO advises against all but essential travel to parts of Togo. |
| 🟢 | [Tonga](countries/tonga.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Trinidad and Tobago](countries/trinidad-and-tobago.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Tunisia](countries/tunisia.md) | FCDO advises against all travel to parts of Tunisia. |
| ⚠️ | [Turkey](countries/turkey.md) | FCDO advises against all travel to parts of Turkey. |
| 🟢 | [Turkmenistan](countries/turkmenistan.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Turks and Caicos Islands](countries/turks-and-caicos-islands.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Tuvalu](countries/tuvalu.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [USA](countries/usa.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Uganda](countries/uganda.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Ukraine](countries/ukraine.md) | FCDO advises against all travel to parts of Ukraine.<br />FCDO advises against all but essential travel to parts of Ukraine. |
| 🟡 | [United Arab Emirates](countries/united-arab-emirates.md) | FCDO advises against all but essential travel to United Arab Emirates. |
| 🟢 | [Uruguay](countries/uruguay.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Uzbekistan](countries/uzbekistan.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Vanuatu](countries/vanuatu.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Venezuela](countries/venezuela.md) | FCDO advises against all travel to parts of Venezuela.<br />FCDO advises against all but essential travel to parts of Venezuela. |
| 🟢 | [Vietnam](countries/vietnam.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Wallis and Futuna](countries/wallis-and-futuna.md) | No specific FCDO travel advisories are currently active. |
| ⚠️ | [Western Sahara](countries/western-sahara.md) | FCDO advises against all travel to parts of Western Sahara. |
| 🔴 | [Yemen](countries/yemen.md) | FCDO advises against all travel to Yemen. |
| 🟢 | [Zambia](countries/zambia.md) | No specific FCDO travel advisories are currently active. |
| 🟢 | [Zimbabwe](countries/zimbabwe.md) | No specific FCDO travel advisories are currently active. |

<!-- FCDO_TABLE_END -->

*Last updated: 2026-04-30 03:18 UTC*

## Usage

Install dependencies and run:

```bash
pip install -r requirements.txt
python get_status.py -o travel_advice.md
```

Options:

- `--test` — run with a small subset of countries
- `-o, --output FILE` — write to file instead of stdout
- `--version` — show version

## Automation

The table above is updated daily at 2 AM UTC by a [GitHub Actions workflow](.github/workflows/update_readme.yml). A separate [test workflow](.github/workflows/test_run.yml) can be triggered manually from the Actions tab.

## Data Source

Travel advice is fetched from the official [FCDO API](https://www.gov.uk/api/content/foreign-travel-advice). Each country's alert status is categorised using the traffic light system above and sorted alphabetically.

## Disclaimer

This tool is for informational purposes only. Always check the official FCDO website at [gov.uk/foreign-travel-advice](https://www.gov.uk/foreign-travel-advice) for the most current and detailed travel advice before making travel decisions.

## Licence

The code in this repository is licensed under the [MIT Licence](LICENSE).

Travel advice data is published by the UK Foreign, Commonwealth & Development Office under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
