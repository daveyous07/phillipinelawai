"""
Philippine Law - Academic Study Materials.
Structured like bar review and law school syllabus coverage.
Based on publicly known scope from Supreme Court bar syllabi and top law school curricula
(UP, Ateneo, San Beda, etc.). Original summaries for RAG retrieval.
"""
# These are educational overviews, not copied from any source

PH_ACADEMIC_DOCUMENTS = [
    # POLITICAL AND INTERNATIONAL LAW (Bar 15%)
    {
        "source": "STUDY MATERIAL - Bar Subject Political and International Law (scope summary)",
        "content": """
        Political and International Law (15% of Bar). Political Law: branch of public law on 
        organization and operations of government and state-inhabitant relations. Covers: 
        Constitutional Law (1987 Constitution, amendments, interpretation); Bill of Rights 
        (due process, equal protection, privacy); separation of powers; fundamental powers 
        (police, eminent domain, taxation); Administrative Law; Law on Public Officers; 
        Municipal Corporations; Election Laws. Public International Law: sources, statehood, 
        treaties, diplomatic immunity, conflict of laws.
        """,
    },
    {
        "source": "STUDY MATERIAL - Political Law Bill of Rights (topic overview)",
        "content": """
        Bill of Rights (Article III): Due process (substantive and procedural; judicial and 
        administrative); equal protection; levels of scrutiny (strict, intermediate, rational basis); 
        privacy and autonomy; right to life, liberty, property; right against unreasonable search 
        and seizure; privacy of communication; freedom of speech and press; freedom of religion; 
        liberty of abode; right to information; right to form associations; non-impairment of contracts; 
        right to counsel and against self-incrimination (Section 12, 17); right to bail; right to 
        speedy trial; writ of habeas corpus.
        """,
    },
    {
        "source": "STUDY MATERIAL - Political Law Three Departments (topic overview)",
        "content": """
        Legislative Department (Article VI): Congress, Senate, House; powers; bill passage. 
        Executive (Article VII): President, powers, appointment, pardon. Judicial (Article VIII): 
        judicial power; Supreme Court; lower courts; judicial review; no doctrine of 
        constitutional supremacy. Constitutional Commissions: Civil Service, COMELEC, COA; 
        independence and fiscal autonomy.
        """,
    },
    # COMMERCIAL AND TAXATION LAWS (Bar 20%)
    {
        "source": "STUDY MATERIAL - Bar Subject Commercial and Taxation Laws (scope)",
        "content": """
        Commercial and Taxation Laws (20% of Bar). Commercial: Corporation Code, Securities 
        Regulation Code, negotiable instruments, sales, insurance, partnership, agency, 
        transportation. Taxation: National Internal Revenue Code; income tax; estate and donor's 
        tax; VAT; percentage tax; remedies (protest, refund, compromise); local taxation; 
        tax exemption and immunity.
        """,
    },
    {
        "source": "STUDY MATERIAL - Corporation Law (key concepts overview)",
        "content": """
        Corporation: artificial being; creation by law; separate juridical personality. Doctrine 
        of piercing the corporate veil when used for fraud. Stockholders' rights: inspection, 
        dividends, preemptive rights. Directors: fiduciary duties; business judgment rule. 
        Ultra vires acts. Dissolution and liquidation.
        """,
    },
    {
        "source": "STUDY MATERIAL - Taxation Law (principles overview)",
        "content": """
        Taxation: power of the state to impose burdens. Principles: lifeblood theory; uniformity; 
        equity; progressive; constitutional limitations. Situs of taxation. Double taxation. 
        Tax exemption strictly construed. CIR's power to interpret; BIR rulings. Assessment 
        presumes correctness; burden on taxpayer. Statute of limitations on collection.
        """,
    },
    # CIVIL LAW (Bar 20%)
    {
        "source": "STUDY MATERIAL - Bar Subject Civil Law (scope)",
        "content": """
        Civil Law (20% of Bar). Civil Code Books: I-Persons (legal personality, family, marriage); 
        II-Property (ownership, possession, usufruct); III-Modes of Acquiring (succession); 
        IV-Obligations and Contracts. Plus: Family Code; Property Registration Decree; 
        Land Titles and Deeds. Persons: capacity, civil status, domicile. Obligations: sources; 
        breach; remedies. Contracts: essential requisites; perfection; rescission; damages.
        """,
    },
    {
        "source": "STUDY MATERIAL - Civil Law Obligations and Contracts (overview)",
        "content": """
        Obligations: juridical necessity to give, do, or not do. Sources: law, contracts, 
        quasi-contracts, delicts, quasi-delicts. Contracts: consent, object, cause. Perfection 
        by consent. Rescissible, voidable, unenforceable, void. Breach remedies: specific 
        performance, rescission, damages (Art. 1170). Solidary obligation; joint and several.
        """,
    },
    {
        "source": "STUDY MATERIAL - Civil Law Succession (overview)",
        "content": """
        Succession: transmission of rights upon death. Testate: through valid will. Intestate: 
        by operation of law. Compulsory heirs and legitime. Order of intestate heirs: 
        descendants, ascendants, collateral, spouse. Wills: notarial, holographic, witnessed. 
        Disinheritance; preterition. Estate settlement; partition.
        """,
    },
    # LABOR LAW (Bar 10%)
    {
        "source": "STUDY MATERIAL - Bar Subject Labor Law (scope)",
        "content": """
        Labor Law (10% of Bar). Labor Code: pre-employment, employment (conditions, benefits, 
        termination), post-employment; labor relations (right to organize, CBA, strike, lockout); 
        disputes. Social legislation: SSS, GSIS, PhilHealth, Pag-IBIG. Construction in favor 
        of labor. Security of tenure; just and authorized causes for dismissal. Due process 
        in termination. Backwages and separation pay.
        """,
    },
    {
        "source": "STUDY MATERIAL - Labor Law Termination (overview)",
        "content": """
        Just causes: serious misconduct, willful disobedience, fraud, loss of confidence, 
        commission of crime, analogous. Authorized: installation of labor-saving devices, 
        redundancy, retrenchment, closing/cessation. Two-notice rule: first notice (show 
        cause), hearing, second notice (decision). Failure to comply = illegal dismissal. 
        Reinstatement or separation pay.
        """,
    },
    # CRIMINAL LAW (Bar 10%)
    {
        "source": "STUDY MATERIAL - Bar Subject Criminal Law (scope)",
        "content": """
        Criminal Law (10% of Bar). Revised Penal Code: felonies, elements, circumstances 
        (justifying, exempting, mitigating, aggravating); crimes against persons, property, 
        chastity; complex crimes. Special penal laws. Criminal Procedure: arrest, search, 
        bail, arraignment, trial. Miranda rights; right to counsel. Presumption of innocence.
        """,
    },
    {
        "source": "STUDY MATERIAL - Criminal Law Felonies (overview)",
        "content": """
        Felony: act or omission punishable by law. Dolo (intent) vs. culpa (fault). Stages: 
        attempted, frustrated, consummated. Justifying: self-defense, defense of relative, 
        Avoidance of evil. Exempting: minority, insanity, irresistible force, uncontrollable 
        fear. Mitigating: provocation, passion, voluntary surrender. Aggravating: treachery, 
        evident premeditation.
        """,
    },
    # REMEDIAL LAW, LEGAL ETHICS (Bar 25%)
    {
        "source": "STUDY MATERIAL - Bar Subject Remedial Law and Ethics (scope)",
        "content": """
        Remedial Law, Legal and Judicial Ethics (25% of Bar). Civil Procedure: jurisdiction, 
        venue, parties, pleadings, trial, judgment, execution, appeal. Criminal Procedure: 
        prosecution, arrest, bail, arraignment, trial. Evidence: admissibility, burden of proof, 
        presumptions, hearsay, best evidence. Special proceedings. Legal Ethics: CPR, duties 
        to client, court, profession. Judicial conduct.
        """,
    },
    {
        "source": "STUDY MATERIAL - Evidence rules (overview)",
        "content": """
        Evidence: means of ascertaining truth. Admissible if relevant and not excluded. 
        Burden of proof: on party who asserts. Presumptions: conclusive vs. disputable. 
        Hearsay rule and exceptions. Best evidence: original for writings. Parol evidence 
        rule: cannot vary written agreement. Expert testimony; character evidence.
        """,
    },
    {
        "source": "STUDY MATERIAL - Legal Ethics CPR (overview)",
        "content": """
        Lawyer's duties: to society, legal profession, courts, clients. Canon 1: Uphold 
        Constitution, obey laws. Duties to client: competence, diligence, confidentiality, 
        conflict of interest. Duties to court: candor, respect. Advertising and solicitation 
        restricted. Withdrawal: mandatory vs. permissive. IBP; mandatory continuing legal education.
        """,
    },
    # ADDITIONAL LAW SCHOOL TOPICS
    {
        "source": "STUDY MATERIAL - Legal Research and Statutory Construction",
        "content": """
        Legal Research: primary sources (Constitution, statutes, jurisprudence); secondary 
        (treatises, journals). Citation: Philippine format. Statutory Construction: verba 
        legis; plain meaning; legislative intent; ejusdem generis; noscitur a sociis; 
        expressio unius; reductio ad absurdum. Ambiguity construed against drafter. Penal 
        laws strictly construed.
        """,
    },
    {
        "source": "STUDY MATERIAL - Philosophy of Law and Jurisprudence",
        "content": """
        Philosophy of Law: natural law vs. legal positivism; purpose of law; justice. 
        Jurisprudence: study of law and legal principles. Schools: natural law (Aquinas); 
        positivism (Austin, Kelsen); legal realism. Philippine context: civilian and common 
        law influence; Spanish and American legal tradition.
        """,
    },
    {
        "source": "STUDY MATERIAL - Clinical Legal Education",
        "content": """
        Clinical Legal Education: supervised practice before bar admission. Law students 
        provide free legal aid under lawyer supervision. Required for JD graduation. 
        Develops skills: client interviewing, legal writing, court appearance. UP Law, 
        Ateneo Law, San Beda, and other schools operate legal aid bureaus serving 
        indigent clients.
        """,
    },
    {
        "source": "STUDY MATERIAL - Bar Exam format and requirements",
        "content": """
        Bar Examinations: 75% general weighted average to pass. Six subjects; 20 questions 
        each. Essay format. Conducted digitally. Political & International 15%; Commercial 
        & Tax 20%; Civil 20%; Labor 10%; Criminal 10%; Remedial & Ethics 25%. Scope: laws, 
        rules, jurisprudence as of cutoff date in Bar Bulletin. Regional testing centers.
        """,
    },
]
