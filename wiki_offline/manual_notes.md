War Doctrines (Battle Doctrines)
Each race contributes a War Doctrine that applies kingdom-wide during War.
Doctrine strength scales with the number of provinces of that race, up to a defined cap.


Global Parameters (Applies to All Races)
Base Value: 1.5%
Increment: +1% per province of that race
Maximum Cap: 7.5%


Design Guardrails
No War Doctrine may exceed 7.5% total effect.
Caps are designed to be reached at 7 provinces, not earlier, except Avians, they reach cap at 5.
Additional provinces beyond the cap do not increase doctrine strength.


Massacre Changes
Massacre effectiveness in War will now be 2x instead of 3x.


Learn and Plunder Changes
Learns and Plunders will have their enemy military kills reverted to normal troop kills in War.


Out of War Attack Penalty Updates
When targeting a Kingdom that is less than 85% of both your Land and Networth, the following penalties apply:
Battle Gains: –10%
Military Casualties: +10%
Honor Gains: –25%
Attack Time: +20%


Dragons

We are providing some new dragons to add some flavour to the current set. Next age, several dragons have been reworked to hit harder, punish sloppy execution, and better define their role on the battlefield. Whether you’re breaking sustain, choking recovery, or forcing mistakes, each dragon now offers a clearer reason to be chosen and a real consequence if ignored.

General Changes
Elites deal dragon damage based on their higher value.
For example, an elite with 14/4 will deal 14 damage per unit to a dragon (before any slaying modifiers apply).
Elites no longer combine offence and defence when slaying dragons. Only the higher of the two values is used.
Dragon HP reduced by 10%.


Amethyst Dragon
−40% Spell Success Chance
−40% Thievery Success Chance on sabotage operations
Enemy provinces suffer +25% thievery and wizard losses on failed spells and sabotage operations
Cost Modifier: 2.4


Emerald Dragon
+25% military casualties in combat
−20% combat gains
−40% Building and Specialist Credits gained in combat
Cost Modifier: 2.4


Celestite Dragon
−60% Birth Rates
−40% Hospital Effectiveness
+50% Build Cost and Time
Cost Modifier: 2.4


Ruby Dragon
Reduces Military Effectiveness by 15%
Increases Military Wages by 30%
Lose 30% of new draftees
Cost Modifier: 2.4


Topaz Dragon
−30% Building Efficiency
−25% Income
Destroys 4% of buildings instantly and every 6 days thereafter
Cost Modifier: 2


Sapphire Dragon
−30% lower magic (WPA) and thievery (TPA) effectiveness
+12.5% Instant Spell and Sabotage Damage taken
−12.5% Instant Spell and Sabotage Damage dealt
Cost Modifier: 2


Rituals

Barrier
+20% Birth Rates
−25% Damage from Enemy Instant Magic and Thievery Operations
−20% Massacre Damage
−10% Battle (Resource) Losses


Expedient
+20% Building Efficiency
−25% Construction Cost
−25% Construction Time
−25% Military Wages


Ascendancy
+50% Wizard Production
−50% Wizard Losses on Failed Spells
−25% Science Book Production


Haste
−10% Attack Time
−25% Training Time
−25% Construction Time


Havoc
+20% Offensive WPA
+20% Offensive TPA
+20% Spell Damage
+20% Sabotage Damage


Onslaught
+10% Offensive Military Efficiency
+15% Enemy Military Casualties on Attacks


Stalwart
+5% Defensive Military Efficiency
−20% Military Casualties


Spell Changes
Greed increased from 25% to 35% for both Wage and Draft Costs.



Resolution of common ambiguities

Resolution for Ambiguity #1 (Stances): > Stances (Aggressive, Peaceful, Normal) no longer exist in Age 114. Therefore, whenever a Wiki formula from Part 3 includes a "Stance Modifier" (such as in the Attack Gains or Rune Generation formulas), that variable must always be calculated as exactly $1.0$ (having no effect). Do not confuse Stances with Relations (Unfriendly, Hostile, War), which are still highly active and apply their respective modifiers.

Resolution for Ambiguity #2 (Multiplicative Modifiers): > Unless explicitly stated otherwise, Race and Personality modifiers are always multiplicative, never additive. When calculating stacked bonuses (or penalties), calculate the Race multiplier and the Personality multiplier separately and multiply them together.

Resolution for Ambiguity #3 (Handling "Unknown" Formulas): > * Building Credits: We will utilize the working formula: $Base Credits = Acres Taken \times 0.4 \times Relative NW$. All known modifiers  will be applied multiplicatively to this base.Propaganda: For attrition models, we recognize Propaganda's yield as a dynamic variable, but we classify it mathematically as a $2x$ Value Swing compared to standard sabotage, because it simultaneously reduces enemy military count and increases our own.

Resolution for Ambiguity #5 (Flat Rate Capacity vs. Production): Production Modifiers: Any modifier affecting "Flat Rate Production" (e.g., Rune or Food generation) acts as a standard multiplier—such as $(1 + Race)$ or $(1 + Personality)$—and is always subject to Building Efficiency (BE). It does not bypass economic penalties.Capacity Modifiers: Any modifier affecting "Capacity" (e.g., population limits, stable space, dungeon space) modifies the base value directly and always ignores Building Efficiency (BE).

Resolution for Ambiguity #6 (Ambush Immunities & War Spoils): Both Anonymity and War Spoils grant complete immunity to being ambushed