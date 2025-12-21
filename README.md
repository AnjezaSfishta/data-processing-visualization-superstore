<table border="0">
 <tr>
    <td style="width:300px; vertical-align:middle; text-align:center;">
      <img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/University_of_Prishtina_logo.svg" 
           alt="University Logo" 
           style="width:250px; height:auto;" />
    </td>
    <td style="vertical-align:middle; padding-left:20px;">
      <h2><strong>Universiteti i Prishtinës</strong></h2>
      <h3>Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike</h3>
      <p>Inxhinieri Kompjuterike dhe Softuerike – Programi Master</p>
      <p><strong>Profesor:</strong> Dr.Sc. Mërgim H. HOTI</p>
    </td>
 </tr>
</table>

---

# Data Processing and Visualization: Superstore Sales Overview

## Përshkrim i përgjithshëm i projektit
Ky projekt realizohet në kuadër të lëndës **“Përgatitja dhe Vizualizimi i të Dhënave”** dhe ka për qëllim përgatitjen, pastrimin, transformimin dhe analizën e të dhënave të shitjeve duke ndjekur faza të strukturuara të punës në Data Science.

Projekti fokusohet në:
- Para-procesimin e të dhënave
- Trajtimin e vlerave mungese dhe duplikateve
- Transformimin dhe krijimin e veçorive të reja
- Diskretizimin, binarizimin dhe standardizimin
- Detektimin dhe mënjanimin e vlerave përjashtuese (outliers)
- Vizualizimin dhe eksplorimin multivariante të të dhënave

---

## Tema e Projektit
**Analiza e të dhënave të shitjeve – Superstore Dataset**

---

## Përshkrimi i Dataset-it
Dataset-i **Superstore Sales** është marrë nga një burim publik (**Kaggle**) dhe përmban të dhëna të shitjeve të simuluara për tregun e Shteteve të Bashkuara të Amerikës.

Edhe pse nuk është plotësisht real, dataset-i përdoret gjerësisht për analiza të biznesit dhe trajnime në fushën e **Data Science** dhe **Business Analytics**.

| Atributi | Detaji |
|--------|--------|
| **Emri i Dataset-it** | Superstore Sales Dataset |
| **Burimi** | Kaggle |
| **Madhësia** | ~2.3 MB |
| **Numri i kolonave** | 18 |
| **Përmbajtja** | Shitje, produkte, klientë, rajone, kategori, data porosie dhe dërgese |

Dataset-i përfshin:
- Informacione për shtete, qytete, rajone dhe kode postare  
- Të dhëna për produktet, kategoritë dhe nën-kategoritë  
- Segmentet e klientëve dhe mënyrat e dërgimit  

## Faza e parë - Para-procesimi i të dhënave 

Qëllimi i kësaj faze është përgatitja e dataset-it për analiza të mëtejshme duke siguruar cilësi, konsistencë dhe strukturë të përshtatshme të të dhënave.

*Rezultati përfundimtar është një dataset i  pastër dhe i gatshëm për përdorim në fazën e dytë të projektit.*

Hapat e fazes se pare:

1. Importimi i librarive 

Është bere importimi i librarive te duhura për përpunimin, analizën dhe vizualizimin e të dhënave.

<img width="285" height="68" alt="image" src="https://github.com/user-attachments/assets/79695911-3a74-4ced-850f-529ecce2c259" />

2. Identifikimi i Tipeve të të Dhënave

Në këtë hap janë analizuar llojet e të dhënave për secilën kolonë për të siguruar përputhshmëri dhe përdorim korrekt në analizat e mëtejshme.

<img width="505" height="607" alt="image" src="https://github.com/user-attachments/assets/d4cae1da-98c2-4f19-ba3b-e336960b5de7" />

3.Identifikimi i Vlerave Null

Figura më poshtë paraqet vizualizimin e vlerave të zbrazëta në dataset para fazës përfundimtare të pastrimit. Vërehet se mungesat janë të përqendruara kryesisht në kolonat Order Date dhe Ship Date, si pasojë e konvertimit të vlerave të pavlefshme në NaT.
<img width="840" height="549" alt="image" src="https://github.com/user-attachments/assets/960e3066-c16e-4a69-8724-ec86552d7fd3" />

4. Trajtimi vlerave Null

Pas identifikimit të vlerave të zbrazëta, u aplikuan teknika të përshtatshme për trajtimin e tyre. Në kolonën Sales, vlerat mungese u zëvendësuan me median për të shmangur ndikimin e vlerave ekstreme. Ndërsa për kolonat Order Date dhe Ship Date, rreshtat që përmbanin data të pavlefshme (NaT) u hoqën, pasi këto të dhëna janë thelbësore për analizat kohore dhe krijimin e veçorive të reja. Ky proces rezultoi në një dataset më të qëndrueshëm dhe pa mungesa kritike të të dhënave.

<img width="643" height="67" alt="image" src="https://github.com/user-attachments/assets/4f6721a9-c9b5-400f-a88f-0ea3939d1006" />


5. Diskretizimi, Binarizimi dhe Standardizimi

Fillimisht, vlerat e shitjeve janë standardizuar për t’i sjellë në një shkallë të përbashkët (me mesatare 0 dhe devijim standard 1).
Më pas, kolona Sales është diskretizuar në katër intervale (Sales_binned), duke kategorizuar nivelet e shitjeve nga më të ulëtat tek më të lartat. Gjithashtu, është krijuar kolona binare Sales_binary, ku vlera 1 përfaqëson shitje mbi mesatare, ndërsa vlera 0 shitje nën mesatare.

<img width="404" height="234" alt="image" src="https://github.com/user-attachments/assets/74115982-507a-4899-8f03-d9a43da1a868" />


6.Reduktimi i dimensioneve me PCA

PCA (**Principal Component Analysis**) është përdorur për të reduktuar dimensionet e të dhënave dhe për të vizualizuar strukturën e tyre në një hapësirë me më pak komponentë.Shpërndarja e vlerave tregon se shumica e porosive janë të përqendruara në vlera të ulëta, ndërsa ekzistojnë disa vlera më të larta që kontribuojnë në variancën totale.

<img width="850" height="547" alt="image" src="https://github.com/user-attachments/assets/d79fa93c-9370-41b1-bee3-500ffbf240dc" />


7.Mostrim dhe Agregim i të Dhënave

Në këtë seksion do të kryejmë disa analiza përmbledhëse duke përdorur funksione të tilla si:
- `groupby()` për të grupuar të dhënat sipas kategorive ose rajoneve
- `agg()` për të llogaritur mesatare, total dhe numërime
- `sample()` për të marrë mostra të rastësishme nga dataset-i

Këto analiza ndihmojnë për të kuptuar shpërndarjen e shitjeve dhe fitimeve sipas rajonit, kategorisë ose segmentit të klientit.
Disa nga rezultatet e agregimit:

<img width="782" height="195" alt="image" src="https://github.com/user-attachments/assets/8e25dd5b-2d48-4422-b357-13aeb7393863" />
<img width="453" height="220" alt="image" src="https://github.com/user-attachments/assets/a03aabb3-c3d7-4212-bd78-6e038a06eff3" />

---

## Faza e dytë – Detektimi i Përjashtuesve dhe Eksplorimi i të Dhënave

Në këtë fazë fokusi është në identifikimin dhe trajtimin e **outlier-ëve** për të përmirësuar cilësinë e analizave.

### Metodat e përdorura për detektimin e outlier-ëve:
- **IQR (Interquartile Range)** – bazuar në kuartile dhe shpërndarjen e të dhënave  
- **Z-score** – bazuar në devijimin nga mesatarja \([-3, 3]\)  
- **Grubbs’ Test** – identifikim statistikor i outlier-ëve individualë  
- **Isolation Forest** – algoritëm i mësimit makinerik për analiza multivariante  

Këto metoda janë përdorur për krahasim dhe analizë të rezultateve ndërmjet tyre.


####  Rezultatet e detektimit te outliers

<img width="420" height="35" alt="image" src="https://github.com/user-attachments/assets/34098459-ca93-404c-8bc0-92a400728d51" /><br>

<img width="454" height="38" alt="image" src="https://github.com/user-attachments/assets/2d3d79e4-90d1-49ef-b102-649d8da2355d" /><br>

<img width="454" height="34" alt="image" src="https://github.com/user-attachments/assets/1582c699-2f49-44d0-80b6-38d22cc02c1a" /><br>


### Menjanimi i outliereve

Isolation Forest u përdor si metoda kryesore për mënjanimin e vlerave jonormale, pasi është e përshtatshme për të dhëna multivariante dhe nuk varet nga supozime të forta statistikore mbi shpërndarjen e të dhënave.


### 4. Analiza e karakteristikave unike të metodës

Si shembull ilustrues është marrë analiza e shitjeve në funksion të kohëzgjatjes së dërgesës (Delivery_Days), pasi kjo veçori paraqet një faktor të rëndësishëm operacional që mund të ndikojë në vlerën e shitjeve dhe përvojën e klientit. Kohëzgjatja e dërgesës lidhet drejtpërdrejt me efikasitetin e logjistikës dhe shpesh përdoret për të vlerësuar performancën e shërbimit.

Siç paraqitet në figurë, pas mënjanimit të vlerave përjashtuese (outlier-ëve) me metodën Isolation Forest, të dhënat shfaqen më të qëndrueshme dhe pa devijime ekstreme. Çdo pikë përfaqëson një porosi individuale, ku vërehet se shitjet janë të shpërndara në mënyrë jo-lineare përgjatë vlerave të ndryshme të Delivery_Days, duke sugjeruar se nuk ekziston një lidhje e fortë lineare ndërmjet këtyre dy variablave.

<img width="765" height="482" alt="image" src="https://github.com/user-attachments/assets/386e1384-fb5d-4da0-9601-e815d49b5410" />

---
## FAZA III – Vizualizimi i të Dhënave

Vizualizimi i të dhënave në këtë projekt është realizuar përmes **Microsoft Power BI**, duke përdorur **vizualizime plotësisht dinamike dhe interaktive**. Të gjitha grafiqet reagojnë në kohë reale ndaj **slicers** dhe **filtrave**, duke mundësuar analizë fleksibile dhe shumë-dimensionale të të dhënave.

### 1. Vizualizimi i Shitjeve sipas Rajonit

Është përdorur një **bar chart dinamik** për të paraqitur **Total Sales (Sales_original)** sipas rajoneve (West, East, Central, South). Ky vizualizim mundëson krahasimin e performancës së shitjeve ndërmjet rajoneve dhe reagon ndaj filtrimit sipas segmentit dhe periudhës kohore.

<img width="418" height="277" alt="image" src="https://github.com/user-attachments/assets/38bb801e-8b77-41a4-b81c-1a2804cd14de" />


### 2. Vizualizimi i Shitjeve sipas Kategorisë

Është përdorur një **bar chart horizontal dinamik** paraqet shpërndarjen e shitjeve sipas kategorive të produkteve (Furniture, Office Supplies, Technology). Vizualizimi lejon identifikimin e kategorisë me kontributin më të lartë në shitje dhe ndryshon automatikisht sipas filtrave të zgjedhur.

<img width="448" height="250" alt="image" src="https://github.com/user-attachments/assets/6f5e8b35-c677-4f23-ab75-7595b1815240" />

### 3. Analiza Kohore e Shitjeve

Është përdorur një **line chart dinamik** për të analizuar trendin e shitjeve gjatë viteve. Ky vizualizim mundëson vëzhgimin e rritjes ose rënies së shitjeve në kohë dhe reagon ndaj filtrimit sipas rajonit, segmentit dhe datës së porosisë.

<img width="423" height="255" alt="image" src="https://github.com/user-attachments/assets/92e1e495-8728-413c-bc60-97ee5694fda0" />


### 4. Vizualizimi Shumë-dimensional (Delivery Days vs Sales)

Është ndërtuar një **scatter plot dinamik**, ku paraqitet marrëdhënia ndërmjet **Delivery_Days** dhe **Sales_original**, me ndarje sipas **Category**. Ky vizualizim mundëson analizën e ndikimit të kohës së dorëzimit në vlerën e shitjeve dhe përfaqëson një analizë shumë-dimensionale të të dhënave.

<img width="659" height="258" alt="image" src="https://github.com/user-attachments/assets/69e14ffc-80bc-4877-877f-a5fbd45ea665" />


### 5. KPI Cards Dinamike

Në dashboard janë shtuar **KPI Cards dinamike** për:
- **Total Sales** (shuma totale e shitjeve)
- **Average Delivery Days** (mesatarja e ditëve të dorëzimit)

Këto KPI reagojnë në kohë reale ndaj të gjitha filtrave dhe ofrojnë një përmbledhje të menjëhershme të performancës së shitjeve.

<img width="240" height="222" alt="image" src="https://github.com/user-attachments/assets/288eb934-d551-4933-bb83-639bc926ef3b" />

  
### 6. Ndërveprimi dhe Filtrimi Dinamik

Dashboard-i përfshin **slicers dinamike** për:
- Rajonin (Region)
- Segmentin e klientëve (Segment)
- Datën e porosisë (Order Date)

Përdoruesi mund të filtrojë të dhënat dhe të analizojë ndikimin e këtyre filtrave në të gjitha vizualizimet njëkohësisht, duke përfituar një përvojë plotësisht interaktive.

<img width="793" height="143" alt="image" src="https://github.com/user-attachments/assets/b0ed0bd8-1f4e-433d-acd9-dd2d4f153a4f" />


## Konkluzioni
Të gjitha vizualizimet në këtë fazë janë **dinamike**, **interaktive** dhe të ndërtuara për të mbështetur analizën eksploruese të të dhënave. Përdorimi i Microsoft Power BI ka mundësuar analizë të avancuar shumë-dimensionale dhe interpretim të qartë të rezultateve.



## Author
- *Anjeza Sfishta*

