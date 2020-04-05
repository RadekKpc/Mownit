import numpy as np
import math
COUNT_OF_FILES = 20


def open_document_to_read(num):
    return open("files/text"+ str(num) +".txt","r")

def load(count):
    words = []
    for i in range(count):
        f = open_document_to_read(i)
        words += f.read().split(' ')
        f.close()
    return words

def create_bag_of_words(words,words_dict,union_size):

    bag = [0 for x in range(union_size)]

    for w in words:
        if w in words_dict.keys():
            bag[words_dict[w]] += 1

    return bag

words = load(COUNT_OF_FILES)
#  changing all string to lower case
for  i, w in enumerate(words):
    words[i] = words[i].lower()

# creating union of wrolds
all_worlds = set(words)
# all_worlds = set(["and","or","beacouse","one","1"])
wrolds_array = []
words_dict = {}

for i,w in enumerate(all_worlds):
    wrolds_array.append(w)
    words_dict[w] = i

union_size = int(len(wrolds_array))

# 3,4 bag-of-worlds vetor for each document and matrix
print("Union size",union_size)
documents = []
for i in range(COUNT_OF_FILES):
    f = open_document_to_read(i)
    words_from_file = f.read().split(' ')
    for  i, w in enumerate(words_from_file):
        words_from_file[i] = words_from_file[i].lower()

    documents.append(create_bag_of_words(words_from_file,words_dict,union_size))

# 5 Przetwórz wstępnie otrzymany zbiór danych mnożąc
# elementy bag-of-words przez inverse document
# frequency. Operacja ta pozwoli na redukcję
# znaczenia często występujących słów.

idf = []
for i,w in enumerate(wrolds_array):
    idf.append(0)
    for doc in range(COUNT_OF_FILES):
        if documents[doc][i] != 0:
            idf[i] += 1
    if(idf[i]!=0):
        idf[i] = math.log(COUNT_OF_FILES/idf[i])


# redukcja znaczenia często występujących słów.

for doc in range(COUNT_OF_FILES):
    for i,w in enumerate(wrolds_array):
        documents[doc][i] *= idf[i]


# k zwrócenie dokumentów najbardziej zbliżonych do podanego zapytania q.
#  Użyj korelacji między wektorami jako miary podobieństwa

# wyznaczenie wtekora q (bag-of-words) ilosci słów w kazdym tekscie

document_to_compare = "including @ @ @ @ @ @ @ @ @ @ Regions *Dn Laoghaire-Rathdown County Council ( 5 ) *Fingal County Council ( 5 ) Like each Regional Authority , the DRA is assisted in its duties by an Operational Committee and EU Operational Committee . # Dissolution of Dublin County Council # Dublin County Council ( which did not include the county borough of Dublin ) was abolished in 1994 and the area divided among the administrative counties of Dn LaoghaireRathdown , Fingal and South Dublin each with its county seat . To these areas may be added the area of Dublin city which collectively comprise the Dublin Region ( ' ' ' ' ) and come under the remit of the Dublin Regional Authority . The area lost its administrative county status in 1994 , with Section 9 Part 1(a) of the ' ' Local Government ( Dublin ) Act , 1993 ' ' stating that the county shall cease to exist . At that time , and in response to a European Council report highlighting Ireland as the most centralised country in the European Union , it was decided that a single County Dublin was unmanageable and undemocratic from @ @ @ @ @ @ @ @ @ @ dissolve Dublin County Council , Avril Doyle TD said , The Bill before us today effectively abolishes County Dublin , and as one born and bred in these parts of Ireland I find it rather strange that we in this House are abolishing County Dublin . I am not sure whether Dubliners realise that that is what we are about today , but in effect that is the case . Despite the legal status of the Dublin Region , the term County Dublin is still in common usage . Many organisations and sporting teams continue to organise on a County Dublin or Dublin Region basis . The area formerly known as County Dublin is now defined in legislation solely as the Dublin Region under the ' ' Local Government Act , 1991 ( Regional Authorities ) ( Establishment ) Order , 1993 ' ' , and this is the terminology officially used by the four Dublin administrative councils in press releases concerning the former county area . The term ' ' Greater Dublin Area ' ' , which might consist of some or all of the Dublin Region along with counties @ @ @ @ @ @ @ @ @ @ standing . The latest Ordnance Survey Ireland Discovery Series ( Third Edition 2005 ) 1:50,000 map of the Dublin Region , Sheet 50 , shows the boundaries of the city and three surrounding counties of the region . Extremities of the Dublin Region , in the north and south of the region , appear in other sheets of the series , 43 and 56 respectively . # Media # * The local radio stations include 98FM , FM104 , 103.2 Dublin City FM , Dublin 's Q102 , Spin 1038 , Dublin 's Country Mix 106.8 , Phantom 105.2 and Radio Nova . * The local newspapers include ' ' Dublin Penny Journal ' ' , ' ' The Echo ' ' , ' ' The Northside People ' ' , ' ' The Southside People ' ' , ' ' Liffey Champion ' ' and ' ' The Metro Herald ' ' . Most of the area can receive the five main UK television channels on analogue television as well as the main Irish channels , along with Sky TV and UPC cable television . # Transport # * Road @ @ @ @ @ @ @ @ @ @ N4 and N7 national primary roads , and the M1 , M11 and M50 motorways . * Heavy rail : The InterCity and Commuter rail services ( Iarnrd ireann ) . * Light rail : The Luas tram system serving Dublin City and its southern and western suburbs . * Rapid transit : The DART and the proposed Dublin Metro line . * Port : Dublin Port and Dn Laoghaire Harbour . * Air : Dublin International Airport . # Economy # The economy of County Dublin was identified as being the powerhouse behind the Celtic Tiger , a period of strong economic growth of the state . This resulted in the economy of the county expanding by almost 100% between the early 1990s and 2007 . This growth resulted from incoming high-value industries , such as financial services and software manufacturing , as well as low-skilled retail and domestic services , which caused a shift away from older manufacturing-industry . This change saw high unemployment in the 1980s and early 1990s which resulted in damage to the capitals social structure . County Dublin 's GDP in 2002 was 42.505bn , @ @ @ @ @ @ @ @ @ @ , and 171% of the European Union average . The workforce of the county in 2003 was 555,306 which equated to a 95.9% employment rate with services ( 80.0% ) , industrial employment ( 12.0% ) , and construction ( 8.0% ) forming the key industries . # Transport # County Dublin is the main transport node of Ireland , and contains one international airport , Dublin Airport . It is also served by two main seaports , Dn Laoghaire port and Dublin Port , which is just located outside of the city center . The two main train stations are Dublin Heuston and Dublin Connolly , both of which serve intercity trains . # Demographics # According to the 2006 census , County Dublin had a population of 1,187,176 , which constitutes 30% of the national population . This was an increase of 9.5% on 2002 figures . Its population density was 1,218/km . The population of Dublin City , was 506,211 . The median age of the population of the county in the 2006 census was 35.6 years , with 62% of people aged between 2064 years old . @ @ @ @ @ @ @ @ @ @ 48,000 , with a natural increase of 33,000 people . There are 10,469 Irish speakers in County Dublin attending the 31 Gaelscoils ( Irish language primary schools ) and eight Gaelcholiste ( Irish language secondary schools ) . There may be up to another 10,000 Irish speakers from the Gaeltacht living and working in Dublin also . # Urban areas # A list of the largest urban areas ( those with over 1,000 inhabitants ) in County Dublin . Administrative county seats are shown in bold . class= wikitable ! Rank ! Urban area ! County ! Population <small> ( 2006 census ) # Towns and suburbs # * Adamstown * Artane * Ashtown * Balbriggan * Baldoyle * Balgriffin * Ballinteer * Ballsbridge * Ballyboden * Ballybrack * Ballybough * Ballyfermot * Ballygall * Ballymount * Ballymun * Ballyroan * Balrothery * Bayside * Beaumont * Belfield * Blackrock * Blanchardstown * Bluebell * Booterstown * Brittas * Broadstone * Ballyboughal * Cabinteely * Cabra * Carrickmines * Castleknock * Chapelizod * Cherrywood * Churchtown * Clondalkin * Clonsilla * Clonskeagh * Clontarf * Coolmine * Coolock * Corduff * @ @ @ @ @ @ @ @ @ @ Deansgrange * Dollymount * Dolphin 's Barn * Donabate * Donaghmede * Donnybrook * Donnycarney * Drimnagh * Drumcondra * Dn Laoghaire * Dundrum * East Wall * Edmondstown * Fairview * Finglas * Firhouse * Foxrock * Garristown * Glasnevin * Glasthule * Glencullen * Glenageary * Goatstown * Grangegorman * Harold 's Cross * Howth * Inchicore * Irishtown * Islandbridge * Jobstown * Kill O ' The Grange * Kilbarrack * Killester * Killiney * Kilmacud * Kilmainham * Kilnamanagh * Kilternan * Kimmage * Kinsealy * Knocklyon * Leopardstown * Loughlinstown * Lucan * Lusk * Malahide * Marino * Milltown * Monkstown * Mount Merrion * Mulhuddart * Newcastle * Naul * Oldbawn * Ongar * Palmerstown * Phibsborough * Portmarnock * Portobello * Raheny * Ranelagh * Rathcoole * Rathfarnham * Rathgar * Rathmichael * Rathmines * Rialto * Ringsend * Rush * Saggart * Sallynoggin * Sandycove * Sandyford * Sandymount * Santry * Shankill * Skerries * Smithfield * Stepaside * Stillorgan * Stoneybatter * Sutton * Swords * Tallaght * Templeogue * Terenure * The Coombe * Tyrrelstown * Walkinstown * Whitechurch @ @ @ @ @@7514 birthplace = notableinstruments = Christine Lavin ( born January 2 , 1952 ) is a New York City-based singer-songwriter and promoter of contemporary folk music . She has recorded numerous solo albums , and has also recorded with other female folk artists under the name Four Bitchin ' Babes . She has also put together several compilation albums of contemporary folk artists , including her latest ' ' Just One Angel ' ' , 22 singer/songwriters singing **30;600955;TOOLONG Year 's songs including actor Jeff Daniels , Grammy-winners Janis Ian and Julie Gold , and the Guitar Man Of Central Park David Ippolito . She is known for her sense of humor , which is expressed in both her music and her onstage performances . Many of her songs alternate between emotional reflections on romance and outright comedy . Two of her more famous songs are Sensitive New Age Guys and Bald Headed Men . One of Lavin 's songs , Regretting What I Said to You When You Called Me 11:00 On a Friday Morning to Tell Me that at 1:00 Friday Afternoon You 're Gon na Leave @ @ @ @ @ @ @ @ @ @ Go Out to the Airport to Catch a Plane to Go Skiing in the Alps for Two Weeks , Not that I Wanted to Go With You , I Was n't Able to Leave Town , I 'm Not a Very Good Skier , I Could n't Expect You to Pay My Way , But After Going Out With You for Three Years I DO N'T Like Surprises ! ! Subtitled : A Musical Apology is notable for having the longest known song title . It is the eighth song on her 1984 album ' ' Future Fossils ' ' , and is 3:04 ( 3 minutes and 4 seconds ) long . In her youth , Lavin was a cheerleader in Peekskill , New York , and she still has impressive baton-twirling skills ; she often ends a concert by twirling a glow-in-the-dark baton with the house lights turned off as she leaves the stage . Lavin worked at Caffe Lena in Saratoga , New York , until Dave Van Ronk convinced her to move to New York City and make a career as a singer-songwriter . She followed his @ @ @ @ @ @ @ @ @ @ has lived in the City ever since . Lavin was the original host of ' ' Sunday Breakfast ' ' on WFUV in New York City . Lavin was a founding member of the Four Bitchin ' Babes when they were formed in 1990 . In recent years Lavin has been known to host knitting circles before her shows , inviting any knitters , hookers ( people who crochet ) , or other crafters to join her . # Awards # * The ASCAP 43rd Annual Deems Taylor Award for her book ' ' Cold Pizza For Breakfast : A Mem-Wha ? ? ' ' , 2011 * The ASCAP Foundation Jamie deRoy and Friends Award , 2010 * Top 100 of the Most Influential Artists in the Last 15 Years , ' ' Singer Songwriter Magazine ' ' * Top 30 iPod Singer/Songwriters of Choice , WUMB , Boston 2006 * ASCAP Composer Award 1992 , 1993 , 1996 , 1998 , 1999 , 2004 , 2005 , 2006 * Singer/Songwriter of the Year , ' ' Back Stage Magazine ' ' , NYC 2001 * Honorable Mention , NAIRD @ @ @ @ @ @ @ @ @ @ ' ' Please Do nt Make Me Too Happy ' ' * New York Music Award Folk Artist of the Year 1990 , 1992 * World Folk Music Association Kate Wolf Memorial Award 1990 * NAIRD Folk Album of the Year , 1988 : ' ' Good Thing He Cant Read My Mind ' ' # Discography # * ' ' Absolutely Live ' ' ( 1981 ; re-issued by Winthrop , 2000 ) * ' ' Future Fossils ' ' ( Philo , 1984 ) * ' ' Beau Woes and Other Problems of Modern Life ' ' ( Philo , 1986 ) * ' ' Another Woman 's Man ' ' ( Philo , 1987 ) * ' ' Good Thing He Ca n't Read My Mind ' ' ( Philo , 1988 ) * ' ' Attainable Love ' ' ( Philo , 1990 ) * ' ' Compass ' ' ( Philo , 1991 ) * ' ' Live at the Cactus Cafe : What Was I Thinking ? ' ' ( Philo , 1993 ) * ' ' Please Do n't Make Me Too Happy ' @ @ @ @ @ @ @ @ @ @ My Flashlight on the Moon ' ' ( Shanachie , 1997 ) * ' ' One Wild Night in Concert ' ' ( 1998 ) * ' ' Getting in Touch With My Inner Bitch ' ' ( Christine Lavin , 1999 ) * ' ' The Bellevue Years ' ' ( Philo , 2000 ) * ' ' The Subway Series ' ' ( Christine Lavin , 2001 )"
document_to_compare = document_to_compare.split(' ')
for  i, w in enumerate(document_to_compare):
    document_to_compare[i] = document_to_compare[i].lower()

compare_doc_bag = create_bag_of_words(document_to_compare,words_dict,union_size)

# print("dlugosc doc: ", len(documents[0]))
# print("dlugosc bag: ", len(compare_doc_bag))

def cos_prob(vec_1,vec_2):
    if len(vec_1) != len(vec_2):
        print("podane wektory nie sa rownej dlugosc")
        exit(0)

    result = 0.0
    for i in range(len(vec_1)):
        result += (vec_1[i]*vec_2[i])

    norma_1 = 0.0
    norma_2 = 0.0
    for i in range(len(vec_1)):
        norma_1 += vec_1[i]**2
        norma_2 += vec_2[i]**2
    norma_1 = math.sqrt(norma_1)
    norma_2 = math.sqrt(norma_2)

    return result/(norma_1*norma_2)

# prownywanie z dokumentami naszego wejsciowego dokumentu
document_comparing = []

for doc in range(COUNT_OF_FILES):
    porb = cos_prob(documents[doc],compare_doc_bag)
    document_comparing.append({'prob' : porb,'doc': doc})

print("Najbardziej podobne dokumnety:")
for d in document_comparing:
    if d['prob'] > 0.1:
        print("files/text" + str(d['doc']) + " podobienstwo: "+ str(d['prob']))


# Normalizacja wektorow cech dj i wektora q nowa miara prawdopodobienstwa


def normalizuj(vec):
    res = []
    norma = 0.0
    for v in vec:
        norma += v**2
    norma = math.sqrt(norma)

    for v in vec:
        res.append(v/norma)

    return res

# normalizacja q i doc
compare_doc_bag = normalizuj(compare_doc_bag)

for i,doc in enumerate(documents):
    documents[i] = normalizuj(doc)

# wektor prawdopodobienstwa
prob_vec = np.dot(documents, compare_doc_bag)
print(list(prob_vec))

# Usuniecie szumu z macierzy A za pomoca SVD
# przykladowe k
k = 3

u,s,vh = np.linalg.svd(documents)

u = np.matrix(u[:,:k])

s = np.diag(s[:k])

vh = np.matrix(vh[:k,:])

prob_matrix = u * s * vh

#  nowa miara prawdopodobienstwa
prob_vec = np.dot(prob_matrix, compare_doc_bag)
prob_vec = np.matrix.tolist(prob_vec)[0]
print(prob_vec)

# Porownujemy wyszukiwanie dla ronyh wartosci K
for k in range(0,COUNT_OF_FILES+1):

    u,s,vh = np.linalg.svd(documents)

    u = np.matrix(u[:,:k])

    s = np.diag(s[:k])

    vh = np.matrix(vh[:k,:])

    prob_matrix = u * s * vh

    prob_vec = np.dot(prob_matrix, compare_doc_bag)
    prob_vec = np.matrix.tolist(prob_vec)[0]
    print("Dla k = ",k,"<br>")
    for i,v in enumerate(prob_vec):
        if v > 0.1:
            print("files/text" + str(i) + " podobienstwo: "+ str(v)+"<br>")












