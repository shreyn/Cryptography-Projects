from MonoalphabeticSub import generate_random_key, encryption, decryption
import string

text = """
iwillnotattempttodescribehowthegentleeyesofagathafilledwithtearsastheirfatherpluckedtheblossomandplaceditinhisdaughtershandsshethankedhiminthemosttenderwayandhehelduphishandsinpraiseofthelovelyflowertheyseemeddeepsympatheticwithallsorrowedandjoysshedrewherchairneartoherfatherandtakinghisheadbetweenherhandskissedhisbrowandplacedthefloweronhisbosomthenthesecretstoftheheartflowedforthinamurmurofgratitudefromherlipsandthetearsfellfromhereyeshefoldedherarmsabouthisneckandlookeduptohimwithaholydevotionmyheartbeatquickthiswassorrowfulandalsofullofjoyiwithdrewwithoutattemptingtodefinewhatifeeliwastoodeeplyaffectedandretiredtoarecessofthecottageitiswithconsiderabledifficultythatiremembertheoriginofmyexistencealltheeventsofthattimeappearconfusedandindistinctamemorywhenihadfirstseenthelightandastillmoreconfusedrecollectionofhavingbeenmovedandslowlyoppresseditwasalongtimenorcanithinkwhatperiodoflifetowhichicanapplythisbutveryearlyindeedinthebeginningiwasasensiblesubstancedistinguishedbythesenseoftouchasitweretofeelpainandsometimespleasureonemythoughtswereconfinedtomyownfeelingsandtheonlyobjectswhichpresseduponmewereplacedorisupposedtobeplacedinmyviewtheseformedmyworldiconfusedlightwhichboundedmeoneverysidewasaftermanyweeksrenderedbydegreesdiscernibleobjectsbywhichimeanproducingdifferentimagestomyfacultiesandleadingmetodistinguishtherelativepositionofseveralsurroundingbodiesinthisstateofchildhoodihadnoideaofthekindofbeingiamorofmyownexistenceandtheonlydistinguishedthingthatfacedmewasatremendouslightwhichhurtnedmeandwhenirefusedtowarditandtherebyclosedmyeyescertainperiodicaldarknessfollowedifeltalsofeelingsofhungerandthirstandwasovercomebysleepthesefeelingsandthesoundsofthebirdsandtherustlingofleaveshadamuchgreatereffectuponmethanthelightscoldandhungerandthirstdistressedmeinexcessbutiwasacquaintedwithnorisubsequentlysoughttheremedyforitibeheldthemoonandthebrightnessofthestarsandsometimesfeltthewindswhistlingaroundmeitheregrewandgainedknowledgealthoughthepathwaspainfulandlonelybutwithtimeigrewmoreintelligentilearnedtosettlemygazeupontheobjectsthatreflectedlightandtoappreciatetheirdistanceandformialsolearntodistinguishmystepsuponthegroundfromthesoftfootfallsandcracklingofbranchesandfinallytolistenattentivelyandsometimeswithpleasuretothesoundsofvoicesiwasasyetignorantofspeechandofeverymodebywhichhumanscommunicatetheirthoughtsifequentlyattemptedtoimitatethemsoundswhichiproceededfromtheirlipsbutweretotallyincapableofarticulatingthemialsoattimeslookedupwithwonderattheskywithitscountlessstarsandthemoonitsorbofsoftandsoothinglightandwatcheditsriseandfallwithinaregularcourseitwasalmostwithgriefthatifoundthatthemoonhadceasedtospreaditslightovermeandwithjoywelcomeditsreturnitpresentedaglowofbeautythatdeeplyaffectedmewhichwasheightenedwhenafteraclapofthunderandaflashoflightningheavyrainsandstormdescendedfromthecloudsandobscuredtheheavenlybodiesproducingatimeofgloomeveninhismomentsofthefiercestdespairitwassuchmomentswhichforcedmetoconfrontmyconditionialonemycreatorhadforsakenmeandmankindspurnedmewhereveriwenttherewasnonewhoextendedawelcominghandnomercifulwordwasutteredinthepresenceofmywretchednessandmyisolationwasechoedinthecoldstarsaboveandtheunfeelingearthbelowbutipressedonhopingthatintimeicouldfindacompanionorbeingwhojudgedmeformyactionsratherthanmyappearanceandmyheartthoughwoundedwasnotyetwhollycorruptedithrobbedwithaffectionateyearningtowardseverycreaturedeemingthatsurelyamongthemillionsofbeingsinhumanformtherewouldbesomeonelivingwhohasnotbeheldmemightlovemeiwasnotsoignorantofhumannatureastoexpecttheymightembracemeallatoncebutimaginedthatbygentlegradualadvancesanddemonstrationsofkindnessimightsoftentheirsuspicionsandbymylanguagewinmysympathybutalasmyhopeswerefutileandeverystepibeganwithtrustwasmetwithdreadorevenviolenceandthebitternessofthistruthsankdeepintomybeingasiponderedthisinevitabletruthiretreatedfromthedwellingsoftheirinhabitantsandhidemyselfinforthsandmountainsinsearchofsolaceinthenaturalworld
"""
ALPHABET = string.ascii_lowercase

ENGLISH_LETTER_FREQ = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.12702,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074
}


key = generate_random_key()
ciphertext = encryption(text, key)


def letter_frequencies(text):
    frequencies = dict()
    textLen = len(text)
    for letter in ALPHABET:
        frequencies[letter] = text.count(letter)
    for letter in frequencies:
        frequencies[letter] = frequencies[letter] / textLen
    return frequencies


cipher_freqs = letter_frequencies(ciphertext)
sorted_cipher_letters = sorted(cipher_freqs, key=cipher_freqs.get, reverse=True)
sorted_english_letters = sorted(ENGLISH_LETTER_FREQ, key=ENGLISH_LETTER_FREQ.get, reverse=True)

guess_mapping = {cipher: plain for cipher, plain in zip(sorted_cipher_letters, sorted_english_letters)}


def apply_guess_mapping(ciphertext, mapping):
    return ''.join(mapping.get(c, c) for c in ciphertext)

guessed_plaintext = apply_guess_mapping(ciphertext, guess_mapping)


true_mapping = {key[i]: ALPHABET[i] for i in range(26)}

# Print comparison table
print("\n--- Comparison: Actual vs Guessed Mapping (Top 10 letters) ---")
print(f"{'Cipher':^8} {'Actual':^8} {'Guessed':^8}")
print("-" * 26)
for c in sorted_cipher_letters[:10]:
    actual = true_mapping[c]
    guessed = guess_mapping[c]
    print(f"{c:^8} {actual:^8} {guessed:^8}")


print("\n--- Guessed Decryption ---")
print(guessed_plaintext[:500])