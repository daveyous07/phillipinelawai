"""
Juris Doctor Program Curriculum - Cotabato State University, College of Law.
Course topics for RAG and test generation. Covers Philippine law and Shariah law.
Source: 2024-2025 curriculum.
"""
# Add more law content for each topic as needed; these serve as topic descriptors

JD_CURRICULUM_DOCUMENTS = [
    # FIRST YEAR
    {"source": "JD Year 1 - Philosophy of Law", "content": "Philosophy of Law: Jurisprudence, legal philosophy, natural law, positivism, and the nature and purpose of law."},
    {"source": "JD Year 1 - Persons and Family Law", "content": "Persons and Family Law: Civil Code provisions on natural persons, family relations, marriage, legal separation, property relations, parental authority, adoption, and support."},
    {"source": "JD Year 1 - Constitutional Law I", "content": "Constitutional Law I: 1987 Philippine Constitution, preamble, national territory, declaration of principles, bill of rights, and citizenship."},
    {"source": "JD Year 1 - Legal Research with Bibliography", "content": "Legal Research with Bibliography: Research methodology, legal citations, primary and secondary sources, and bibliography for Philippine law."},
    {"source": "JD Year 1 - Statutory Construction", "content": "Statutory Construction: Rules of interpretation, legislative intent, canons of construction, and application of statutes."},
    {"source": "JD Year 1 - Criminal Law I", "content": "Criminal Law I: Revised Penal Code, felonies, elements of crimes, exempting and justifying circumstances, and crimes against persons."},
    {"source": "JD Year 1 - Shariah Law I", "content": "Shariah Law I - Introduction to Islamic Law and Jurisprudence: Sources of Islamic law, Quran, Sunnah, Ijma, Qiyas, and Islamic legal schools."},
    {"source": "JD Year 1 - Law and Islamic Morality", "content": "Law and Islamic Morality: Intersection of Islamic ethics, Shariah principles, and Philippine secular law."},
    {"source": "JD Year 1 - Obligations and Contracts", "content": "Obligations and Contracts: Civil Code Book IV on obligations, contracts, prestations, sources of obligations, and contract formation."},
    {"source": "JD Year 1 - Constitutional Law II", "content": "Constitutional Law II: Legislative, executive, judicial departments, constitutional commissions, local government, and amendments."},
    {"source": "JD Year 1 - Environmental and Natural Resources Law", "content": "Environmental and Natural Resources Law: Clean Air Act, Clean Water Act, Environmental Code, mining, forestry, and land use."},
    {"source": "JD Year 1 - Criminal Law II", "content": "Criminal Law II: Crimes against property, crimes against chastity, and other offenses under the Revised Penal Code."},
    {"source": "JD Year 1 - Basic Legal and Judicial Ethics", "content": "Basic Legal and Judicial Ethics: Code of Professional Responsibility, duties of lawyers, judicial ethics, and canons."},
    {"source": "JD Year 1 - Shariah Law II", "content": "Shariah Law II - Persons and Family Relations: Islamic law on marriage, divorce, custody, inheritance under Muslim Personal Laws."},
    {"source": "JD Year 1 - Clinical Legal Education 1", "content": "Clinical Legal Education 1: Supervised legal aid, client interviewing, and community legal assistance."},
    # SECOND YEAR
    {"source": "JD Year 2 - Public International Law", "content": "Public International Law: Sources, statehood, treaties, diplomatic immunity, and relations between states."},
    {"source": "JD Year 2 - Civil Procedure I", "content": "Civil Procedure I: Rules of Court on jurisdiction, venue, parties, pleadings, and pretrial in civil cases."},
    {"source": "JD Year 2 - Agency, Trust and Partnership Law", "content": "Agency, Trust and Partnership Law: Agency, trust, partnership under the Civil Code and special laws."},
    {"source": "JD Year 2 - Corporation and Securities Law", "content": "Corporation and Securities Law: Corporation Code, Securities Regulation Code, corporate governance, and stockholders' rights."},
    {"source": "JD Year 2 - Labor Law and Social Legislation", "content": "Labor Law and Social Legislation: Labor Code, employment, termination, collective bargaining, social security, and benefits."},
    {"source": "JD Year 2 - Criminal Procedure", "content": "Criminal Procedure: Rules on criminal prosecution, arrest, search and seizure, trial, and appeal in criminal cases."},
    {"source": "JD Year 2 - Shariah Law III", "content": "Shariah Law III - Inheritance, Wills and Adjudication of Estates: Islamic succession, distribution of estate, and wills under Muslim law."},
    {"source": "JD Year 2 - Administrative Law and Law on Public Officers", "content": "Administrative Law and Law on Public Officers: Administrative agencies, due process, public office, and accountability."},
    {"source": "JD Year 2 - Civil Procedure II", "content": "Civil Procedure II: Trial, judgment, execution, appeal, and special proceedings."},
    {"source": "JD Year 2 - Property and Land Law", "content": "Property and Land Law: Ownership, possession, land registration, public land, and agrarian reform."},
    {"source": "JD Year 2 - Basic Succession Law", "content": "Basic Succession Law: Testate and intestate succession, wills, legacies, and estate settlement."},
    {"source": "JD Year 2 - Taxation Law", "content": "Taxation Law: National Internal Revenue Code, income tax, VAT, estate tax, and tax remedies."},
    {"source": "JD Year 2 - Commercial Laws I", "content": "Commercial Laws I: Negotiable instruments, sales, insurance, and other commercial transactions."},
    {"source": "JD Year 2 - Shariah Law IV", "content": "Shariah Law IV - Procedure and Evidence: Islamic courts, procedure, and rules of evidence in Shariah proceedings."},
    # THIRD YEAR
    {"source": "JD Year 3 - Laws on Local Government", "content": "Laws on Local Government: Local Government Code, powers of LGUs, barangay, municipality, city, province, and ARMM/BARMM."},
    {"source": "JD Year 3 - Evidence", "content": "Evidence: Rules of Evidence, admissibility, witnesses, documentary evidence, and burden of proof."},
    {"source": "JD Year 3 - Private International Law", "content": "Private International Law: Conflict of laws, jurisdiction, choice of law, and recognition of foreign judgments."},
    {"source": "JD Year 3 - Commercial Laws 2", "content": "Commercial Laws 2: Partnership, corporation, securities, and other commercial law topics."},
    {"source": "JD Year 3 - Special Rules and Proceedings", "content": "Special Rules and Proceedings: Rules on small claims, barangay conciliation, and other special proceedings."},
    {"source": "JD Year 3 - Parliamentary Legislation", "content": "Elective - Parliamentary Legislation: Legislative process, bill drafting, and parliament in the Bangsamoro context."},
    {"source": "JD Year 3 - Transitional Justice System", "content": "Elective - Transitional Justice System: Transitional justice, reparations, and post-conflict legal frameworks."},
    {"source": "JD Year 3 - Election Laws", "content": "Election Laws: Omnibus Election Code, Comelec powers, suffrage, and electoral procedures."},
    {"source": "JD Year 3 - Medical Jurisprudence", "content": "Medical Jurisprudence: Legal aspects of medical practice, malpractice, consent, and forensic medicine."},
    {"source": "JD Year 3 - Torts and Damages", "content": "Torts and Damages: Quasi-delicts, negligence, damage computation, and civil liability."},
    {"source": "JD Year 3 - Gender Sensitivity and Laws on Women and Children", "content": "Gender Sensitivity and Laws on Women and Children's Rights: VAWC, Magna Carta of Women, child protection laws."},
    {"source": "JD Year 3 - Legal Writing and Forms", "content": "Legal Writing and Forms: Pleadings, motions, briefs, and legal document drafting."},
    {"source": "JD Year 3 - Practice Court", "content": "Practice Court: Moot court, trial advocacy, and simulated court proceedings."},
    {"source": "JD Year 3 - Bangsamoro Election Law", "content": "Elective - Bangsamoro Election Law: Electoral framework in the Bangsamoro region."},
    {"source": "JD Year 3 - Legal Ethics in Bangsamoro Region", "content": "Elective - Special Areas in Legal Ethics in the Bangsamoro Region: Ethics in legal practice within BARMM context."},
    {"source": "JD Year 3 - Clinical Legal Education 2", "content": "Clinical Legal Education Program 2: Advanced clinical training and community legal service."},
    # FOURTH YEAR
    {"source": "JD Year 4 - Political and International Law Review", "content": "Political and International Law Review: Bar review on constitutional law, political law, and international law."},
    {"source": "JD Year 4 - Civil Law Review", "content": "Civil Law Review: Bar review on persons, family, obligations, contracts, property, succession, and civil law."},
    {"source": "JD Year 4 - Criminal Law Review", "content": "Criminal Law Review: Bar review on Revised Penal Code and special penal laws."},
    {"source": "JD Year 4 - Labor Law Review", "content": "Labor Law Review: Bar review on Labor Code and labor legislation."},
    {"source": "JD Year 4 - Legal and Judicial Ethics Review", "content": "Legal and Judicial Ethics Review and Practical Exercises: Bar review on professional responsibility and judicial ethics."},
    {"source": "JD Year 4 - Remedial Law Review", "content": "Remedial Law Review: Bar review on civil procedure, criminal procedure, evidence, and special proceedings."},
    {"source": "JD Year 4 - Commercial Law Review", "content": "Commercial Law Review: Bar review on commercial laws, corporation, taxation, and related topics."},
    {"source": "JD Year 4 - Taxation Law Review", "content": "Taxation Law Review: Bar review on tax laws and tax remedies."},
]
