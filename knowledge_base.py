"""
Scriptural Knowledge Base for Shree Krishna Life Guide.
Includes curated verses, translations, philosophical frameworks,
and stories from the Vedas, Upanishads, Puranas, Ramayana, Mahabharata, and Bhagavad Gita.
"""

from typing import List, Dict, Any

SCRIPTURE_DATA: List[Dict[str, Any]] = [
    # ==========================================
    # 💼 BUSINESS, LEADERSHIP, DECISION MAKING & STRATEGY
    # ==========================================
    {
        "id": "gita_2_47",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 2, Verse 47",
        "sanskrit": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।\nमा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥",
        "transliteration": "karmaṇy-evādhikāras te mā phaleṣu kadācana |\nmā karma-phala-hetur bhūr mā te saṅgo 'stv akarmaṇi ||",
        "translation": "You have a right to perform your prescribed duties, but you are not entitled to the fruits of action. Never consider yourself the cause of the results of your activities, and never be attached to inaction.",
        "domains": ["business", "mental_health", "spiritual"],
        "topics": ["work ethic", "anxiety", "results", "startups", "failure", "stress", "execution", "focus"],
        "essence": "Focus 100% of your intellect and energy on the quality of your execution today. Anxiety arises when you mentally live in an uncertain future outcome instead of mastering the present action.",
        "practical_application": "In business and careers, detached excellence produces superior results because your mind is freed from the paralyzing fear of failure and obsessive greed for outcomes."
    },
    {
        "id": "gita_3_21",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 3, Verse 21",
        "sanskrit": "यद्यदाचरति श्रेष्ठस्तत्तदेवेतरो जनः।\nस यत्प्रमाणं कुरुते लोकस्तदनुवर्तते॥",
        "transliteration": "yad yad ācarati śreṣṭhas tat tad evetaro janaḥ |\nsa yat pramāṇaṁ kurute lokas tad anuvartate ||",
        "translation": "Whatever action a great leader performs, common men follow. Whatever standards he sets by exemplary acts, all the world pursues.",
        "domains": ["business", "relationships"],
        "topics": ["leadership", "culture", "role model", "team management", "integrity", "ethics"],
        "essence": "True leadership is not exercised through command and coercion, but through unassailable personal conduct and standard-setting.",
        "practical_application": "If you wish your team or organization to be punctual, transparent, bold, and empathetic, you must embody those traits first without compromise."
    },
    {
        "id": "gita_18_47",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 18, Verse 47",
        "sanskrit": "श्रेयान्स्वधर्मो विगुणः परधर्मात्स्वनुष्ठितात्।\nस्वभावनियतं कर्म कुर्वन्नाप्नोति किल्बिषम्॥",
        "transliteration": "śreyān sva-dharmo viguṇaḥ para-dharmāt sv-anuṣṭhitāt |\nsva-bhāva-niyataṁ karma kurvan nāpnoti kilbiṣam ||",
        "translation": "It is far better to perform one’s own duty, even if imperfectly, than to attempt another's duty perfectly. By doing duties ordained by one's own nature (Sva-bhava), one incurs no stain.",
        "domains": ["business", "mental_health", "spiritual"],
        "topics": ["career choice", "authenticity", "comparison", "imposter syndrome", "calling", "strengths"],
        "essence": "Never build a career or business merely by imitating what is fashionable or lucrative for others. True fulfillment and enduring mastery lie in aligning your work with your inherent nature (Sva-dharma).",
        "practical_application": "Identify your unique innate skills and inclinations. Operating against your natural grain causes chronic burnout; operating in alignment brings effortless flow and resilience."
    },
    {
        "id": "gita_18_26",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 18, Verse 26",
        "sanskrit": "मुक्तसङ्गोऽनहंवादी धृत्युत्साहसमन्वितः।\nसिद्ध्यसिद्ध्योर्निर्विकारः कर्ता सात्त्विक उच्यते॥",
        "transliteration": "mukta-saṅgo 'nahaṁ-vādī dhṛty-utsāha-samanvitaḥ |\nsiddhy-asiddhyor nirvikāraḥ kartā sāttvika ucyate ||",
        "translation": "The worker who is free from selfish attachment and ego, endowed with steadfast determination and intense enthusiasm, and unruffled by success or failure, is called Sattvic (noble and enlightened).",
        "domains": ["business", "mental_health"],
        "topics": ["grit", "resilience", "equanimity", "professionalism", "startups", "enthusiasm"],
        "essence": "The ideal executive or creator possesses a rare combination: high enthusiasm and relentless drive, coupled with emotional neutrality towards temporary wins and losses.",
        "practical_application": "Celebrate victories without hubris; analyze setbacks without self-pity. Keep enthusiasm high while shedding ego."
    },
    {
        "id": "vidura_niti_1",
        "source": "Mahabharata (Udyoga Parva)",
        "chapter_verse": "Vidura Niti 33.16",
        "sanskrit": "आत्मज्ञानं समारम्भस्तितिक्षा धर्मनित्यता।\nयमर्था नापकर्षन्ति स वै पण्डित उच्यते॥",
        "transliteration": "ātma-jñānaṁ samārambhas titikṣā dharma-nityatā |\nyam arthā nāpakarṣanti sa vai paṇḍita ucyate ||",
        "translation": "He whose undertakings are based on self-knowledge, exertion, endurance, and firm adherence to righteous principles, and who is never diverted by desire or wealth, is truly wise.",
        "domains": ["business", "relationships", "spiritual"],
        "topics": ["strategic wisdom", "prudence", "counsel", "financial discipline", "endurance"],
        "essence": "Before undertaking any enterprise, assess your capabilities honestly, prepare for hardship with patience, and never sacrifice enduring ethics for quick profit.",
        "practical_application": "Do due diligence, stress-test your business plans, ensure moral clarity, and resist short-term predatory gains."
    },

    # ==========================================
    # 🤝 RELATIONSHIPS, COMPASSION, FAMILY & BOUNDARIES
    # ==========================================
    {
        "id": "gita_6_32",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 6, Verse 32",
        "sanskrit": "आत्मौपम्येन सर्वत्र समं पश्यति योऽर्जुन।\nसुखं वा यदि वा दुःखं स योगी परमो मतः॥",
        "transliteration": "ātmaupamyena sarvatra samaṁ paśyati yo 'rjuna |\nsukhaṁ vā yadi vā duḥkhaṁ sa yogī paramo mataḥ ||",
        "translation": "He is considered the supreme yogi who, by comparison to his own self, sees the true equality of all beings, feeling their joy and sorrow as his own.",
        "domains": ["relationships", "mental_health", "spiritual"],
        "topics": ["empathy", "compassion", "kindness", "marriage", "conflict resolution", "listening"],
        "essence": "The highest emotional intelligence is seeing yourself in the other person. When you recognize that their fears, sensitivities, and desires for happiness are identical to yours, hostility vanishes.",
        "practical_application": "In arguments, pause and ask: 'If I were carrying their upbringing, unhealed wounds, and present pressures, how would I feel?' Respond to their pain, not just their anger."
    },
    {
        "id": "gita_12_13_14",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 12, Verses 13-14",
        "sanskrit": "अद्वेष्टा सर्वभूतानां मैत्रः करुण एव च।\nनिर्ममो निरहङ्कारः समदुःखसुखः क्षमी॥\nसन्तुष्टः सततं योगी यतात्मा दृढनिश्चयः।\nमय्यर्पितमनोबुद्धिर्यो मद्भक्तः स मे प्रियः॥",
        "transliteration": "adveṣṭā sarva-bhūtānāṁ maitraḥ karuṇa eva ca |\nnirmamo nirahaṅkāraḥ sama-duḥkha-sukhaḥ kṣamī ||\nsantuṣṭaḥ satataṁ yogī yatātmā dṛḍha-niścayaḥ |\nmayy arpita-mano-buddhir yo mad-bhaktaḥ sa me priyaḥ ||",
        "translation": "One who is not envious but is a kind friend to all living entities, free from possessiveness and false ego, equal in sorrow and joy, forgiving, always contented, self-controlled, and firmly resolute—such a devotee is very dear to Me.",
        "domains": ["relationships", "mental_health", "spiritual"],
        "topics": ["forgiveness", "unconditional love", "letting go", "possessiveness", "toxic attachments"],
        "essence": "Love becomes toxic when it turns into 'nirmama' (possessiveness) and control. Divine love grants freedom, forgives human frailties, and seeks the partner's genuine growth.",
        "practical_application": "Release the urge to control or reshape your loved ones. Support them unconditionally while maintaining your own inner sanctuary of contentment."
    },
    {
        "id": "ramayana_vibhisana",
        "source": "Valmiki Ramayana (Yuddha Kanda)",
        "chapter_verse": "Sharanagati Shloka 18.33",
        "sanskrit": "सकृदेव प्रपन्नाय तवास्मीति च याचते।\nअभयं सर्वभूतेभ्यो ददाम्येतद् व्रतं मम॥",
        "transliteration": "sakṛd eva prapannāya tavāsmīti ca yācate |\nabhayaṁ sarva-bhūtebhyo dadāmy etad vrataṁ mama ||",
        "translation": "To anyone who surrenders unto Me even once, saying 'I am yours,' and seeks My shelter, I grant freedom from fear against all beings. This is My eternal vow.",
        "domains": ["relationships", "spiritual"],
        "topics": ["shelter", "loyalty", "trust", "forgiveness", "boundaries", "refuge"],
        "essence": "Lord Rama accepted Vibhishana even when all counselors suspected him. True nobility welcomes those who seek genuine reform and redemption.",
        "practical_application": "Judge people by their present sincerity and moral choices, not by their past heritage or associates."
    },

    # ==========================================
    # 🧠 MENTAL PEACE, ANXIETY, EMOTIONAL MASTERY & RESILIENCE
    # ==========================================
    {
        "id": "gita_2_56",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 2, Verse 56",
        "sanskrit": "दुःखेष्वनुद्विग्नमनाः सुखेषु विगतस्पृहः।\nवीतरागभयक्रोधः स्थितधीर्मुनि रुच्यते॥",
        "transliteration": "duḥkheṣv anudvigna-manāḥ sukheṣu vigata-spṛhaḥ |\nvīta-rāga-bhaya-krodhaḥ sthita-dhīr munir ucyate ||",
        "translation": "One whose mind remains unperturbed in misery, who does not crave after happiness, and who is free from attachment, fear, and anger, is known as a sage of steady intellect (Sthitaprajna).",
        "domains": ["mental_health", "spiritual", "business"],
        "topics": ["anxiety", "depression", "emotional stability", "equanimity", "overthinking", "calm"],
        "essence": "Suffering is not caused by external events, but by the mind's violent resistance to painful events and desperate clinging to pleasurable ones.",
        "practical_application": "Cultivate the witness state (*Sakshi Bhava*). When crisis strikes, observe the emotion as a cloud passing through your consciousness without reacting impulsively."
    },
    {
        "id": "gita_2_62_63",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 2, Verses 62-63",
        "sanskrit": "ध्यायतो विषयान्पुंसः सङ्गस्तेषूपजायते।\nसङ्गात्सञ्जायते कामः कामात्क्रोधोऽभिजायते॥\nक्रोधाद्भवति सम्मोहः सम्मोहात्स्मृतिविभ्रमः।\nस्मृतिभ्रंशाद् बुद्धिनाशो बुद्धिनाशात्प्रणश्यति॥",
        "transliteration": "dhyāyato viṣayān puṁsaḥ saṅgas teṣūpajāyate |\nsaṅgāt sañjāyate kāmaḥ kāmāt krodho 'bhijāyate ||\nkrodhād bhavati sammohaḥ sammohāt smṛti-vibhramaḥ |\nsmṛti-bhraṁśād buddhi-nāśo buddhi-nāśāt praṇaśyati ||",
        "translation": "While contemplating sense objects, attachment arises. From attachment develops longing desire, and from unfulfilled desire springs anger. From anger arises delusion, from delusion confusion of memory; with the destruction of memory, the intellect is ruined; and when intellect is ruined, the person is lost.",
        "domains": ["mental_health", "relationships", "business"],
        "topics": ["anger management", "addiction", "delusion", "overthinking", "lust", "impulsivity"],
        "essence": "This is the precise psychological autopsy of human self-destruction. It begins with innocently dwelling upon an object, person, or fantasy in the mind.",
        "practical_application": "Guard the gates of your attention. If you catch desire or anger in its seedling stage, you prevent catastrophic breakdowns of judgment."
    },
    {
        "id": "gita_6_5_6",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 6, Verses 5-6",
        "sanskrit": "उद्धरेदात्मनात्मानं नात्मानमवसादयेत्।\nआत्मैव ह्यात्मनो बन्धुरात्मैव रिपुरात्मनः॥\nबन्धुरात्मात्मनस्तस्य येनात्मैवात्मना जितः।\nअनात्मनस्तु शत्रुत्वे वर्तेतात्मैव शत्रुवत्॥",
        "transliteration": "uddhared ātmanātmānaṁ nātmānam avasādayet |\nātmaiva hy ātmano bandhur ātmaiva ripur ātmanaḥ ||\nbandhur ātmātmanas tasya yenātmaivātmanā jitaḥ |\nanātmanas tu śatrutve vartetātmaiva śatru-vat ||",
        "translation": "Elevate yourself through the power of your own mind, and do not degrade yourself. For the mind alone is the friend of the self, and the mind alone is the enemy of the self. For one who has conquered the mind, it is the greatest friend; but for one who has failed to do so, the mind acts as the worst enemy.",
        "domains": ["mental_health", "spiritual", "physical_health"],
        "topics": ["self-discipline", "depression", "self-sabotage", "mindset", "inner strength", "habits"],
        "essence": "Nobody outside of you has the power to defeat you until your own mind surrenders to defeatism. You must become your own loyal ally.",
        "practical_application": "Stop negative self-talk. Train your intellect to guide your unruly impulses like a loving, disciplined mentor."
    },
    {
        "id": "gita_6_35",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 6, Verse 35",
        "sanskrit": "असंशयं महाबाहो मनो दुर्निग्रहं चलम्।\nअभ्यासेन तु कौन्तेय वैराग्येण च गृह्यते॥",
        "transliteration": "asaṁśayaṁ mahā-bāho mano durnigrahaṁ calam |\nabhyāsena tu kaunteya vairāgyeṇa ca gṛhyate ||",
        "translation": "O mighty-armed son of Kunti, without doubt the mind is turbulent and extremely difficult to curb. But by persistent practice (Abhyasa) and healthy detachment (Vairagya), it can be mastered.",
        "domains": ["mental_health", "physical_health", "spiritual"],
        "topics": ["focus", "meditation", "adhd", "distraction", "discipline", "habits"],
        "essence": "Shree Krishna validates that the restless mind is indeed difficult to tame—even for a warrior like Arjuna. But it yields to two eternal tools: relentless daily practice and releasing toxic cravings.",
        "practical_application": "Do not get disheartened when meditation or focus feels hard. Every time the mind wanders, gently bring it back without frustration (Abhyasa). Reduce mindless stimulation (Vairagya)."
    },

    # ==========================================
    # 🌿 PHYSICAL HEALTH, ENERGY, AYURVEDIC BALANCE & VITALITY
    # ==========================================
    {
        "id": "gita_6_16_17",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 6, Verses 16-17",
        "sanskrit": "नात्यश्नतस्तु योगोऽस्ति न चैकान्तमनश्नतः।\nन चातिस्वप्नशीलस्य जाग्रतो नैव चार्जुन॥\nयुक्ताहारविहारस्य युक्तचेष्टस्य कर्मसु।\nयुक्तस्वप्नावबोधस्य योगो भवति दुःखहा॥",
        "transliteration": "nāty-aśnatas tu yogo 'sti na caikāntam anaśnataḥ |\nna cāti-svapna-śīlasya jāgrato naiva cārjuna ||\nyuktāhāra-vihārasya yukta-ceṣṭasya karmasu |\nyukta-svapnāvabodhasya yogo bhavati duḥkha-hā ||",
        "translation": "Yoga is not possible for one who overeats, nor for one who fasts excessively; it is not for one who sleeps too much, nor for one who stays awake unnaturally. But for one who is moderate in eating and recreation, balanced in work, and regulated in sleep and waking, yoga destroys all sorrow.",
        "domains": ["physical_health", "mental_health"],
        "topics": ["diet", "sleep", "balance", "lifestyle", "burnout", "wellness", "fitness"],
        "essence": "The body is the sacred temple and instrument (*Kshetra*) of the soul. Extremism—whether sensory indulgence or harsh self-punishment—destroys vitality. Health is a harmony of rhythmic moderation.",
        "practical_application": "Align with circadian rhythms: eat fresh, nourishing food in moderation, sleep 7-8 restful hours, engage in daily movement, and balance intense labor with rejuvenating leisure."
    },
    {
        "id": "gita_17_8",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 17, Verse 8",
        "sanskrit": "आयुःसत्त्वबलारोग्यसुखप्रीतिविवर्धनाः।\nरस्याः स्निग्धाः स्थिरा हृद्या आहाराः सात्त्विकप्रियाः॥",
        "transliteration": "āyuḥ-sattva-balārogya-sukha-prīti-vivardhanāḥ |\nrasyāḥ snigdhāḥ sthirā hṛdyā āhārāḥ sāttvika-priyāḥ ||",
        "translation": "Foods that augment life span, clarify the mind, bestow strength, health, happiness, and satisfaction; which are juicy, succulent, wholesome, and pleasing to the heart, are dear to those in the mode of goodness (Sattva).",
        "domains": ["physical_health", "mental_health"],
        "topics": ["nutrition", "sattvic diet", "energy", "gut health", "longevity"],
        "essence": "What you consume directly constructs your mind. Sattvic food provides calm, clean, sustained vitality without digestive sluggishness or erratic blood-sugar crashes.",
        "practical_application": "Prioritize seasonal fresh fruits, vegetables, whole grains, nuts, cold-pressed oils, and clean water. Avoid stale, ultra-processed, overly pungent or chemically loaded foods."
    },
    {
        "id": "taittiriya_annam",
        "source": "Taittiriya Upanishad",
        "chapter_verse": "Bhrigu Valli 3.2.1",
        "sanskrit": "अन्नं ब्रह्मेति व्यजानात्। अन्नाद्ध्येव खल्विमानि भूतानि जायन्ते।\nअन्नेन जातानि जीवन्ति। अन्नं प्रयन्त्यभिसंविशन्तीति॥",
        "transliteration": "annaṁ brahmeti vyajānāt | annādd hy eva khalv imāni bhūtāni jāyante |\nannena jātāni jīvanti | annaṁ prayanty abhisaṁviśantīti ||",
        "translation": "He realized that food (matter/nourishment) is Brahman (the divine). For from food all creatures are born; by food they are sustained; and into food they re-enter.",
        "domains": ["physical_health", "spiritual"],
        "topics": ["food reverence", "mindful eating", "nutrition", "body-mind connection"],
        "essence": "Food is not merely caloric fuel; it is a direct sacred exchange with cosmic energy. Eating with gratitude and calm awareness heals the physical sheath (*Annamaya Kosha*).",
        "practical_application": "Eat without screens, chew thoroughly, offer your meal in gratitude, and treat physical nourishment as an act of worship."
    },

    # ==========================================
    # 🕉️ SPIRITUAL AWAKENING, PURPOSE, KARMA & LIBERATION
    # ==========================================
    {
        "id": "gita_9_22",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 9, Verse 22",
        "sanskrit": "अनन्याश्चिन्तयन्तो मां ये जनाः पर्युपासते।\nतेषां नित्याभियुक्तानां योगक्षेमं वहाम्यहम्॥",
        "transliteration": "ananyāś cintayanto māṁ ye janāḥ paryupāsate |\nteṣāṁ nityābhiyuktānāṁ yoga-kṣemaṁ vahāmy aham ||",
        "translation": "To those who always remember Me with undivided devotion, meditating on My transcendental form, to them who are constantly attuned, I personally carry what they lack and preserve what they have (Yoga-Kshemam Vahamyaham).",
        "domains": ["spiritual", "mental_health", "business"],
        "topics": ["faith", "divine surrender", "security", "anxiety", "abundance", "trust"],
        "essence": "When you align your will with divine order and surrender neurotic self-obsession, the universe shoulders the burden of your welfare. You are never abandoned.",
        "practical_application": "Give your best in every arena, but root your security in the Divine rather than in fluctuating bank accounts, volatile markets, or human opinions."
    },
    {
        "id": "gita_18_66",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 18, Verse 66",
        "sanskrit": "सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज।\nअहं त्वा सर्वपापेभ्यो मोक्षयिष्यामि मा शुचः॥",
        "transliteration": "sarva-dharmān parityajya mām ekaṁ śaraṇaṁ vraja |\nahaṁ tvā sarva-pāpebhyo mokṣayiṣyāmi mā śucaḥ ||",
        "translation": "Abandon all varieties of secondary duties and simply surrender unto Me alone. I shall liberate you from all sinful reactions and distress; do not grieve.",
        "domains": ["spiritual", "mental_health"],
        "topics": ["ultimate surrender", "peace", "liberation", "forgiveness of past", "freedom from guilt"],
        "essence": "The climactic promise of the Bhagavad Gita: Stop carrying the agonizing weight of moral over-analysis, past remorse, and existential guilt. Surrender your burdens to Krishna.",
        "practical_application": "Release past shame and regret. Consecrate your heart to the Supreme, breathe deeply, and step forward into righteous action without fear."
    },
    {
        "id": "isha_upanishad_1",
        "source": "Isha Upanishad",
        "chapter_verse": "Verse 1",
        "sanskrit": "ईशा वास्यमिदं सर्वं यत्किञ्च जगत्यां जगत्।\nतेन त्यक्तेन भुञ्जीथा मा गृधः कस्यस्विद्धनम्॥",
        "transliteration": "īśā vāsyam idaṁ sarvaṁ yat kiñca jagatyāṁ jagat |\ntena tyaktena bhuñjīthā mā gṛdhaḥ kasya svid dhanam ||",
        "translation": "All this—whatever exists in this changing universe—is enveloped by the Supreme Lord. Therefore, enjoy and protect through renunciation; do not covet the wealth of anyone.",
        "domains": ["spiritual", "business", "relationships"],
        "topics": ["contentment", "wealth stewardship", "environmental harmony", "detachment", "greed"],
        "essence": "You do not own this world; you are its honored guest and custodian. True joy (*bhunjitha*) is experienced through generous non-possessiveness (*tyaktena*).",
        "practical_application": "Create abundance, generate wealth, but see yourself as a trustee rather than an arrogant owner. Share freely and envy none."
    },
    {
        "id": "katha_upanishad_chariot",
        "source": "Katha Upanishad",
        "chapter_verse": "1.3.3 - 1.3.4",
        "sanskrit": "आत्मानं रथिनं विद्धि शरीरं रथमेव तु।\nबुद्धिं तु सारथिं विद्धि मनः प्रग्रहमेव च॥\nइन्द्रियाणि हयानाहुर्विषयांस्तेषु गोचरान्।",
        "transliteration": "ātmānaṁ rathinaṁ viddhi śarīraṁ ratham eva tu |\nbuddhiṁ tu sārathiṁ viddhi manaḥ pragraham eva ca ||\nindriyāṇi hayān āhur viṣayāṁs teṣu gocarān |",
        "translation": "Know the Self (Atman) as the master of the chariot, the body as the chariot itself, the intellect (Buddhi) as the charioteer, and the mind (Manas) as the reins. The senses are the horses, and the sense objects are the pathways.",
        "domains": ["spiritual", "mental_health", "physical_health"],
        "topics": ["chariot allegory", "self-mastery", "buddhi", "senses", "clarity", "inner leadership"],
        "essence": "If the intellect (charioteer) is intoxicated or asleep, the mind (reins) goes slack, and the wild senses (horses) plunge the chariot off the cliff. Mastery requires an awake, discerning intellect.",
        "practical_application": "Strengthen your Buddhi (discerning intellect) through daily study and meditation. Let your intellect guide the mind, not the other way around."
    },
    {
        "id": "gita_2_3",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 2, Verse 3",
        "sanskrit": "क्लैब्यं मा स्म गमः पार्थ नैतत्त्वय्युपपद्यते।\nक्षुद्रं हृदयदौर्बल्यं त्यक्त्वोत्तिष्ठ परन्तप॥",
        "transliteration": "klaibyaṁ mā sma gamaḥ pārtha naitat tvayy upapadyate |\nkṣudraṁ hṛdaya-daurbalyaṁ tyaktvottiṣṭha paran-tapa ||",
        "translation": "Do not yield to unmanliness and impotence, O Partha; it does not befit you! Cast off this petty faint-heartedness and rise, O scorcher of enemies!",
        "domains": ["business", "mental_health", "spiritual"],
        "topics": ["courage", "overcoming self-pity", "action", "resilience", "empowerment"],
        "essence": "Shree Krishna's thunderous roar to an Arjuna paralyzed by emotional confusion. He will not tolerate self-pity masquerading as virtue. You are endowed with divine strength—stand up and fulfill your duty.",
        "practical_application": "When overwhelmed by grief or self-doubt, recognize it as temporary weakness of heart. Wipe your tears, invoke your inner warrior, and confront your challenges boldly."
    },
    {
        "id": "gita_11_33",
        "source": "Bhagavad Gita",
        "chapter_verse": "Chapter 11, Verse 33",
        "sanskrit": "तस्मात्त्वमुत्तिष्ठ यशो लभस्व जित्वा शत्रून् भुङ्क्ष्व राज्यं समृद्धम्।\nमयैवैते निहताः पूर्वमेव निमित्तमात्रं भव सव्यसाचिन्॥",
        "transliteration": "tasmāt tvam uttiṣṭha yaśo labhasva jitvā śatrūn bhuṅkṣva rājyaṁ samṛddham |\nmayaivaite nihatāḥ pūrvam eva nimitta-mātraṁ bhava savya-sācin ||",
        "translation": "Therefore rise up, gain glory, conquer your enemies, and enjoy a flourishing kingdom! By Me alone have they already been ordained; be merely My instrument, O ambidextrous archer!",
        "domains": ["business", "mental_health", "spiritual"],
        "topics": ["burnout", "instrument", "ego", "burden", "surrender", "pressure", "overwhelm"],
        "essence": "You do not carry the solitary burden of holding up the entire cosmos. Cosmic destiny is already in motion; you are called simply to be an unblemished, courageous flute through which the divine song plays.",
        "practical_application": "Release the crushing anxiety of thinking 'Everything depends only on my shoulders.' Do your work with joyous freedom as an instrument of divine purpose."
    },
    {
        "id": "yaksha_prashna_wonder",
        "source": "Mahabharata (Vana Parva)",
        "chapter_verse": "Yaksha Prashna 313.116",
        "sanskrit": "अहन्यहनि भूतानि गच्छन्ति यममन्दिरम्।\nशेषाः स्थावरमिच्छन्ति किमाश्चर्यमतः परम्॥",
        "transliteration": "ahany-ahani bhūtāni gacchanti yama-mandiram |\nśeṣāḥ sthāvaram icchanti kim āścaryam ataḥ param ||",
        "translation": "Every single day countless beings depart to the abode of death; yet those who remain believe they will live forever. What can be more wondrous and astonishing than this delusion?",
        "domains": ["spiritual", "mental_health", "business"],
        "topics": ["mortality", "perspective", "procrastination", "clarity", "ego", "urgency"],
        "essence": "Remembering the inevitability and unpredictability of mortality (*Mrityu-bodha*) cuts through petty squabbles, trivial anxieties, and false arrogance like a razor.",
        "practical_application": "Whenever you are stressed over office politics, social slights, or hoarding wealth, remember: this breath is a gift, and life is fleeting. Spend your days on what truly endures."
    },
    {
        "id": "charaka_samhita_swastha",
        "source": "Charaka Samhita",
        "chapter_verse": "Sutra Sthana 21.36",
        "sanskrit": "समदोषः समाग्निश्च समधातुमलक्रियः।\nप्रसन्नात्मेन्द्रियमनाः स्वस्थ इत्यभिधीयते॥",
        "transliteration": "sama-doṣaḥ samāgniś ca sama-dhātu-mala-kriyaḥ |\nprasannātmendriya-manāḥ svastha ity abhidhīyate ||",
        "translation": "One whose physical doshas are in equilibrium, whose digestive fire (Agni) is balanced, whose tissues and excretions function smoothly, and whose Soul, Senses, and Mind are joyful and serene—such a person is called truly Healthy (Svastha).",
        "domains": ["physical_health", "mental_health"],
        "topics": ["ayurveda", "holistic health", "gut health", "vitality", "mind body", "wellness"],
        "essence": "True health (*Svastha* = established in one's true Self) is not merely the absence of disease, but a vibrant state of joyful inner serenity, balanced digestion, and mental delight.",
        "practical_application": "Care for your digestive fire (*Jatharagni*): avoid erratic snacking, honor your circadian rhythms, keep your senses rested, and maintain a cheerful heart."
    },
    {
        "id": "chandogya_tat_tvam_asi",
        "source": "Chandogya Upanishad",
        "chapter_verse": "6.8.7 (Mahavakya)",
        "sanskrit": "स य एषोऽणिमैतदात्म्यमिदं सर्वं तत्सत्यं स आत्मा तत्त्वमसि श्वेतकेतो॥",
        "transliteration": "sa ya eṣo 'ṇimaitad-ātmyam idaṁ sarvaṁ tat satyaṁ sa ātmā tat tvam asi śvetaketo ||",
        "translation": "That subtle essence which is the Soul of this entire universe—That is Truth! That is the Atman! That Thou Art (Tat Tvam Asi), O Shvetaketu!",
        "domains": ["spiritual", "mental_health"],
        "topics": ["mahavakya", "true identity", "fearlessness", "self-realization", "oneness"],
        "essence": "You are not this transient bag of flesh, bones, and neurotic anxieties. You are the infinite, unkillable consciousness that illuminates the entire universe.",
        "practical_application": "Whenever you feel small, unworthy, or shattered by worldly events, remember your true nature. You are the eternal ocean; your thoughts and failures are merely passing ripples on the surface."
    }
]

STOP_WORDS = {
    "a", "an", "the", "and", "or", "in", "on", "at", "to", "for", "with", "by", "about",
    "against", "between", "into", "through", "during", "before", "after", "above", "below",
    "from", "up", "down", "in", "out", "off", "over", "under", "again", "further", "then",
    "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own",
    "same", "so", "than", "too", "very", "can", "will", "just", "should", "now", "what",
    "does", "feel", "like", "deeply", "being"
}

def search_scriptures(query: str, domain: str = None, top_k: int = 3) -> List[Dict[str, Any]]:
    """
    Search scriptural verses by keyword, topic match, or domain filter.
    """
    query_lower = query.lower()
    query_tokens = [w.strip(".,?!\"'()") for w in query_lower.split() if len(w) > 2 and w.lower() not in STOP_WORDS]
    scored = []
    
    for item in SCRIPTURE_DATA:
        score = 0
        
        # Domain boost
        if domain and domain != "all" and domain in item.get("domains", []):
            score += 4
            
        # Exact topic match
        for topic in item.get("topics", []):
            topic_lower = topic.lower()
            if topic_lower in query_lower:
                score += 10
            elif any(token in topic_lower for token in query_tokens):
                score += 4
                
        # Text matches for meaningful tokens
        for token in query_tokens:
            if token in item.get("translation", "").lower():
                score += 2
            if token in item.get("essence", "").lower():
                score += 3
            if token in item.get("practical_application", "").lower():
                score += 3
            if token in item.get("source", "").lower() or token in item.get("chapter_verse", "").lower():
                score += 5
                
        scored.append((score, item))
        
    scored.sort(key=lambda x: x[0], reverse=True)
    return [item for score, item in scored[:top_k]]
