"""
Philippine Supreme Court landmark cases - Jurisprudence.
Under Art. 8, Civil Code: judicial decisions applying/interpreting laws form part of the 
Philippine legal system. These are court rulings, not statutory text.
"""
# Type: JURISPRUDENCE - Supreme Court decisions (law). Distinguished from interpretations.

PH_CASES_DOCUMENTS = [
    # CONSTITUTIONAL LAW
    {
        "source": "JURISPRUDENCE - Hacienda Luisita v. PARC, G.R. No. 171101 (2011)",
        "content": """
        Hacienda Luisita Inc. v. Presidential Agrarian Reform Council (PARC). The Supreme Court addressed 
        agrarian reform compliance under the 1987 Constitution. It ruled on the validity of the stock 
        distribution plan versus direct land distribution to farmworker-beneficiaries. The case established 
        that the Constitution mandates equitable distribution of agricultural lands and that stock 
        distribution must genuinely vest ownership in beneficiaries. Property rights under the Constitution 
        must yield to the state's agrarian reform objectives.
        """,
    },
    {
        "source": "JURISPRUDENCE - People v. Yupo, G.R. No. L-38975 (1980)",
        "content": """
        People v. Paquito Yupo. The Court dismissed use of an extrajudicial confession obtained without 
        counsel present during custodial investigation. The constitutional right to counsel under Article III 
        Section 12 cannot be waived. Any waiver must be in writing and in the presence of counsel. 
        Confessions obtained in violation of this right are inadmissible in evidence.
        """,
    },
    {
        "source": "JURISPRUDENCE - People v. Ramos, G.R. No. 85215 (1989)",
        "content": """
        People v. Felipe Ramos. The Court distinguished the right against self-incrimination from the 
        right to remain silent and have counsel during investigation. Section 20 (now Section 17), 
        Article III protects against coerced testimony. These are separate constitutional protections; 
        violation of one does not automatically violate the other.
        """,
    },
    {
        "source": "JURISPRUDENCE - Ho Wai Pang v. People, G.R. No. 176229 (2011)",
        "content": """
        Ho Wai Pang v. People. Violations of Miranda Rights render only extrajudicial confessions 
        inadmissible. Other evidence obtained during custodial investigation—such as physical evidence 
        or testimony from other witnesses—remains admissible if relevant and not otherwise excluded. 
        The exclusionary rule applies to the confession itself, not necessarily to derivative evidence.
        """,
    },
    {
        "source": "JURISPRUDENCE - Anucension v. National Labor Union, G.R. No. L-26097 (1977)",
        "content": """
        Anucension v. National Labor Union. The Court declared Republic Act No. 3350 unconstitutional 
        for improperly excluding Iglesia ni Cristo members from labor organization coverage. The law 
        violated the constitutional guarantee of religious freedom. Union security clauses cannot 
        override fundamental rights. Labor rights and religious freedom must be balanced.
        """,
    },
    {
        "source": "JURISPRUDENCE - Cuartocruz v. Active Works, G.R. No. 219689 (2019)",
        "content": """
        Arlene Cuartocruz v. Active Works, Inc. The Court declared unconstitutional provisions of 
        RA 8042 (Migrant Workers Act) that limited separation pay awards for overseas workers. 
        Doubts in labor law must be resolved in favor of labor. The Constitution protects the 
        rights of Filipino workers, including OFWs, to full and adequate protection.
        """,
    },
    {
        "source": "JURISPRUDENCE - Kilusang Mayo Uno v. Aquino III, G.R. No. 210761 (2016)",
        "content": """
        Kilusang Mayo Uno v. Benigno S. Aquino III. The Supreme Court addressed PhilHealth premium 
        contribution adjustments. It involved constitutional principles on essential services, 
        social justice, and the state's duty to promote the right to health. The case examined 
        the Philippine Health Insurance Corporation's authority relative to constitutional guarantees.
        """,
    },
    # ADMINISTRATIVE LAW
    {
        "source": "JURISPRUDENCE - Ang Tibay v. CIR, G.R. No. L-46496 (1940)",
        "content": """
        Ang Tibay v. CIR. The Ang Tibay Doctrine sets the seven requisites of administrative due process:
        (1) right to hearing and to present evidence; (2) tribunal must consider evidence; (3) decision 
        must have support; (4) evidence must be substantial; (5) decision on evidence in record disclosed 
        to parties; (6) tribunal must independently consider facts and law; (7) in controversial matters, 
        body must explain issues and reasons. "To be heard" may be through pleadings, not only oral argument.
        """,
    },
    # OBLIGATIONS AND CONTRACTS / CIVIL LAW
    {
        "source": "JURISPRUDENCE - Francisco v. Ferrer, Jr., G.R. No. 142029",
        "content": """
        Francisco v. Ferrer, Jr. Moral and exemplary damages in breach of contract require proof of 
        bad faith, wanton, reckless, malicious, oppressive, or abusive conduct with clear and 
        convincing evidence. Exemplary damages cannot be claimed as matter of right. In a wedding 
        cake case involving negligence, the Court awarded only nominal damages (₱10,000) instead of 
        moral and exemplary damages due to absence of bad faith, despite contractual breach.
        """,
    },
    {
        "source": "JURISPRUDENCE - PEZA v. Pilhino Sales Corp., G.R. No. 185765",
        "content": """
        Philippine Economic Zone Authority v. Pilhino Sales Corporation. Even if contractual provisions 
        are legally null and void, the stipulated method of computing liquidated damages may be accepted 
        as evidence of the parties' intent and can serve as factual basis for awarding damages. 
        Liquidated damages clauses reflect the parties' pre-estimate of loss.
        """,
    },
    {
        "source": "LAW - Civil Code (RA 386) Art. 1170 - Breach of obligation",
        "content": """
        Article 1170. Those who in the performance of their obligations are guilty of fraud, 
        negligence, or delay and those who in any manner contravene the tenor thereof, are 
        liable for damages. Remedies for breach: specific performance, rescission, or damages.
        """,
    },
    # LABOR LAW
    {
        "source": "JURISPRUDENCE - Philippine Association of Free Labor Unions v. Secretary of Labor",
        "content": """
        Philippine Association of Free Labor Unions v. Secretary of Labor. Landmark case on government 
        intervention in labor disputes. Clarified the scope of constitutionally protected labor rights 
        under the Industrial Peace Act regarding strikes and self-organization. The state may intervene 
        to ensure industrial peace while respecting the right to strike.
        """,
    },
    # ELECTION LAWS
    {
        "source": "JURISPRUDENCE - Macalintal v. COMELEC, G.R. No. 157013 (2003)",
        "content": """
        Macalintal v. Commission on Elections. The Court ruled on the constitutionality of provisions 
        of the Overseas Absentee Voting Act. Addressed questions on COMELEC's powers, voter 
        qualification of overseas Filipinos, and the constitutional right of suffrage. Established 
        parameters for absentee voting implementation.
        """,
    },
    # EVIDENCE
    {
        "source": "LAW - Rules of Court, Rules on Evidence - Hearsay",
        "content": """
        Hearsay evidence is generally inadmissible. Exceptions include: dying declaration, 
        declaration against interest, act or declaration about pedigree, family reputation, 
        common reputation, part of the res gestae, entries in the course of business, and others 
        under the Rules of Evidence. The rule ensures reliability and cross-examination of witnesses.
        """,
    },
    {
        "source": "LAW - Rules of Court, Rules on Evidence - Best Evidence",
        "content": """
        When the subject of inquiry is the contents of a writing, the original must be produced. 
        Secondary evidence may be admitted when the original is lost, destroyed, or cannot be 
        produced in court. The best evidence rule applies to documents; parole evidence cannot 
        generally alter the terms of a written agreement.
        """,
    },
    # LOCAL GOVERNMENT
    {
        "source": "JURISPRUDENCE - Local Government Code (RA 7160) - Municipal liability",
        "content": """
        Under the Local Government Code, local government units have corporate powers. They may 
        sue and be sued. Liability for acts of local officials depends on whether the act was 
        official or ultra vires. The doctrine of qualified immunity may apply to local officials 
        performing discretionary functions in good faith.
        """,
    },
    # TORTS AND DAMAGES
    {
        "source": "LAW - Civil Code (RA 386) Art. 2176 - Quasi-delict",
        "content": """
        Article 2176, Civil Code: whoever by act or omission causes damage to another, there being 
        fault or negligence, is obliged to pay for the damage done. This is quasi-delict. The 
        elements are: (1) damage to the plaintiff; (2) fault or negligence of the defendant; 
        (3) causal connection between fault and damage. Liability is solidary among joint tortfeasors.
        """,
    },
    # SUCCESSION
    {
        "source": "LAW - Civil Code Book III - Succession (testate and intestate)",
        "content": """
        Testate succession is when the deceased left a valid will. Intestate succession applies 
        when there is no will or the will is invalid. The law on compulsory heirs and legitime 
        applies in both. Wills must comply with formalities under the Civil Code. Intestate 
        heirs inherit in the order prescribed by law.
        """,
    },
    # FAMILY LAW
    {
        "source": "JURISPRUDENCE - Santos v. CA - Family Law, Nullity of Marriage",
        "content": """
        Marriage may be annulled or declared void on grounds under the Family Code. Psychological 
        incapacity under Article 36 requires evidence of a serious incapacity that existed at the 
        time of marriage and is incurable. The Court has applied strict standards; mere difficulty, 
        irreconcilable differences, or incompatibility do not suffice.
        """,
    },
    # TAXATION
    {
        "source": "JURISPRUDENCE - CIR v. CA and Manila Mining - Taxation",
        "content": """
        Tax assessments are presumed correct. The burden of proof to overturn an assessment rests 
        on the taxpayer. In tax cases, the CIR's factual findings are generally respected if 
        supported by substantial evidence. Tax exemptions are strictly construed against the 
        taxpayer; taxation is the rule, exemption the exception.
        """,
    },
    # SHARIAH / MUSLIM LAW
    {
        "source": "LAW - PD 1083 (Code of Muslim Personal Laws) - Shariah",
        "content": """
        Presidential Decree 1083 (Code of Muslim Personal Laws) governs Muslims in the Philippines 
        on personal and family relations. Shariah District Courts have jurisdiction over certain 
        matters. The Code covers marriage, divorce, custody, support, inheritance, and waqf. 
        It operates alongside the Civil Code where applicable; Muslim law prevails in covered areas.
        """,
    },
    # CORPORATION LAW
    {
        "source": "JURISPRUDENCE - Piercing the corporate veil (Corporation Code interpretation)",
        "content": """
        The corporate veil may be pierced when the corporation is used to commit fraud, 
        evade obligations, or defeat public convenience. Bad faith must be shown. Mere 
        ownership of stock and control is insufficient. The alter ego doctrine applies 
        when the corporation is a mere instrumentality of the stockholder with no 
        separate identity.
        """,
    },
    # REMEDIAL LAW / CIVIL PROCEDURE
    {
        "source": "LAW/JURISPRUDENCE - Res judicata (Rules of Court and case law)",
        "content": """
        Res judicata bars re-litigation of the same claim between the same parties. Two types: 
        (1) bar by former judgment—claim or demand is precluded; (2) conclusiveness of judgment—
        issues actually litigated and determined cannot be re-litigated. Requisites: final judgment, 
        court of competent jurisdiction, identity of parties, identity of subject matter and cause of action.
        """,
    },
]
