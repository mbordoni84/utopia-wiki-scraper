# Utopia Wiki - Age 117

---

# Part 1: Manual Notes (Authoritative)

> **PRIORITY: HIGHEST — Overrides everything else.**
> These notes are manually maintained and reflect the current age's confirmed rules.
> If any information in Part 2 or Part 3 conflicts with this section, discard it and trust Part 1.

# Age 117 Authoritative Data

> These statements are the correct Age 117 values. The Age Details page in Part 2 is scraped from the live game and still contains a few known errors on the points below. Wherever Part 2 (or Part 3) disagrees with this section, this section is correct.

## Races

- **Dark Elf** is immune to Sabotage Wizards. Its unique spells are **Blizzard** and **Mind Focus** only — it does not have Mage's Fury, and Blizzard is listed only once.
- **Dryad** maximum War Doctrine is **+7.5% Offensive Military Efficiency** (+0.75% per province), not +10%.
- **Dwarf** has **-20% Damage Taken from Raze** attacks.
- **Human** has **-20% Military Wages** (a reduction). It is not +20%.
- **Gnome** unique ability **Cunning Assault:** each successful attack provides one of the following thievery boosts, which last for 6 days: **+25% offensive thievery effectiveness, -25% thief losses, or +10% sabotage damage.** All of these can be active at the same time.
- **Undead** is **immune to the Plague only**. It does not always carry the plague. Its Plaguebearers unique ability still gives every successful attack a 33% chance to spread plague to the target province.

## Personalities

- **Tactician** has **100% successful espionage operations at 2x stealth**. It does not grant "no thief losses on intel".
- **Rogue** grants an **offensive Thievery Per Acre (TPA) bonus only** (not defensive).

## Rituals

- The **Ascendency** ritual does **not** exist in Age 117. Ignore any mention of it. The only rituals are: Barrier, Benediction, Haste, Havoc, Onslaught, Stalwart.

## Dragons

- There is **no Amethyst dragon** in Age 117. The only dragons are: **Emerald, Ruby, Sapphire, Topaz**.

---

# Resolution of Common Ambiguities

These resolve recurring mechanics questions. They are timeless rules for interpreting the formulas in Part 3.

## Ambiguity #1 — Stances
Stances (Aggressive, Peaceful, Normal) no longer exist. Whenever a Part 3 wiki formula includes a "Stance Modifier" (such as in Attack Gains or Rune Generation), that variable is always exactly **1.0** (no effect). Do not confuse Stances with Relations (Unfriendly, Hostile, War), which are still active and apply their respective modifiers.

## Ambiguity #2 — Multiplicative Modifiers
Unless explicitly stated otherwise, Race and Personality modifiers are always **multiplicative**, never additive. When stacking bonuses or penalties, compute the Race multiplier and the Personality multiplier separately and multiply them together.

## Ambiguity #3 — Handling "Unknown" Formulas
- **Building Credits:** use the working formula `Base Credits = Acres Taken x 0.4 x Relative NW`. All known modifiers apply multiplicatively to this base.
- **Propaganda:** its yield is a dynamic variable, classified mathematically as a **2x value swing** compared to standard sabotage, because it simultaneously reduces enemy military count and increases your own.

## Ambiguity #5 — Flat Rate Capacity vs. Production
- **Production Modifiers:** any modifier affecting "Flat Rate Production" (e.g. Rune or Food generation) acts as a standard multiplier such as `(1 + Race)` or `(1 + Personality)`, and is always subject to Building Efficiency (BE). It does not bypass economic penalties.
- **Capacity Modifiers:** any modifier affecting "Capacity" (e.g. population limits, stable space, dungeon space) modifies the base value directly and always ignores Building Efficiency (BE).

## Ambiguity #6 — Ambush Immunities & War Spoils
Both Anonymity and War Spoils grant complete immunity to being ambushed.

---

# Part 2: Age Details — Races & Personalities

> **PRIORITY: HIGH — Current age data, second only to Part 1.**
> This page is scraped directly from the game for the current age.
> It is the authoritative source for race stats, personality stats, war doctrines, and unique abilities.
> If Part 3 contradicts this section on any race or personality detail, trust Part 2.

Source: https://utopia-game.com/wol/chooser/age_details/

Utopia
            -

    Age 117: Devoted Pursuits Crowned Promise

Forum
Rules
Merch
Wiki
Blog

### Unique Abilities

Each Race and Personality has a unique ability that reflects its core strengths and theme. These abilities are categorised as either Passive, Active (With duration), Active(Consumable Effect).

- Passive: Always active, provide a consistent positive effect.

- Active (Duration): Activated, Duration is a set amount of days, this works same as Self Spells.

- Active (Consumable): Activated, works until EITHER used or the next day. Be careful using close to a days end!

- Cooldown: Starts when activated and are exact.

### War Doctrines

Each Race provides a unique War Doctrine bonus when your kingdom is at war. The strength of the bonus depends on how many provinces of that race are in your kingdom.

- Base Effect: The starting bonus provided by having at least one province of this race.

- Per Province: Additional bonus gained for each province of this race in your kingdom.

- Maximum: The cap on the total bonus, regardless of how many provinces you have.

Example: If your kingdom has 5 Avian provinces and Avian's War Doctrine is "Attack Time" (Base: 2.0%, Per Province: 1.5%, Max: 12.5%), your kingdom would receive an 8.0% reduction in attack time during war.

Races

### Avian

#### Bonuses:

-20% Attack Travel Time
+25% Birth Rate

#### Penalties:

Can't use Stables or War Horses

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Griffins | (12, 0) |  |
Harpies | (0, 10) |  |
Drakes | (14, 3) | 900gc | 6.25
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (0, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Town Watch

#### War Doctrines

-1.5% **Attack time**, scaling by -0.75% per province of this race in your kingdom (max -7.5%).

#### Unique - Opportunistic Raiders

Avians are masters of lightning-fast raids and resource acquisition. Their natural agility and aerial advantage allow them to swoop in, steal science books or plunder gold, and escape before the enemy can mount a proper defense.

##### Passive Effect

Learn and Plunder attacks return armies 1 tick faster (after modifiers).

### Dark Elf

#### Bonuses:

+20% Combat Instant Spell Damage
-25% Rune Cost (excluding Ritual)
Immune to Sabotage Wizards

#### Penalties:

-20% Sabotage Damage

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Night Rangers | (11, 0) |  |
Druids | (0, 11) |  |
Drows | (13, 4) | 900gc | 6.25
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (2, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Blizzard and Mind Focus

#### War Doctrines

+2% **Instant spell damage**, scaling by +1% per province of this race in your kingdom (max +10%).

#### Unique - Mystic Enthusiasts

Dark Elves possess an innate understanding of the arcane arts, allowing them to channel magical energy with remarkable efficiency. Their mastery over offensive magic enables them to recover a portion of the runes expended, turning successful spellcasting into a sustainable art of war.

##### Passive Effect

Successful offensive instant spells refund 30% of the rune cost.

### Dryad

#### Bonuses:

+25% Dragon slaying strength
+10% Offensive Military Efficiency

#### Penalties:

-10% Building Efficiency

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Huldras | (10, 0) |  |
Nymphs | (0, 9) |  |
Will O The Wisps | (15, 3) | 925gc | 6.75
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (2, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Fanaticism

#### War Doctrines

+1.5% **Offensive military efficiency**, scaling by +0.75% per province of this race in your kingdom (max +7.5%).

#### Unique - Interdiction

Tacticians excel at disrupting enemy logistics and resource chains. Every successful attack in war systematically destroys enemy supplies, cutting off their ability to sustain prolonged conflict.

##### Passive Effect

Successful Attacks in War destroy 15% of enemy gold, 15% of enemy runes, and 15% of enemy food.

### Dwarf

#### Bonuses:

+25% Building Credits
+20% Building Efficiency
-50% Building Construction Cost
-20% Damage Taken from Raze Attacks

#### Penalties:

+50% Food Consumption

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Warriors | (10, 0) |  |
Axemen | (0, 10) |  |
Berserkers | (13, 5) | 950gc | 6.5
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (2, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Miner's Mystique

#### War Doctrines

+2% **Building Efficiency**, scaling by +1% per province of this race in your kingdom (max +10%).

#### Unique - Construction Delays

The Artisan understands the intricate workings of infrastructure and knows precisely where to strike to cause maximum disruption. A successful attack doesn't just destroy buildings—it sabotages supply lines, damages tools, and demoralizes craftsmen, leaving the enemy's economy crippled long after the battle ends.

##### Passive Effect

For 3 ticks after a successful attack, the target's building efficiency is reduced by 10% (does not stack with multiple attacks).

### Elf

#### Bonuses:

+25% Wizards Per Acre (WPA)
+1% Extra Mana Per Tick (in war)
+50% Land Effect - Towers

#### Penalties:

-20% Thieves Per Acre (Offensive Only)

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Rangers | (9, 0) |  |
Archers | (0, 11) |  |
Elf Lords | (5, 12) | 1,000gc | 7.0
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (2, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Pitfalls and Greater Protection

#### War Doctrines

-4% **Defensive Military Casualties**, scaling by -2% per province of this race in your kingdom (max -20%).

#### Unique - Arcane Respite

The din of battle softens to a measured hush. Wards settle, focus returns, and the aether gathers in steady pulses. What was spent flows back, day by day, restoring the will to shape the fight ahead.

##### Active Effect

Once activated, for the next 6 days, regenerate +2 mana per day.

##### Cooldown

23 Utopian Days

##### Duration

6 Utopian Days

### Faery

#### Bonuses:

+25% Offensive Spell Duration
+1% Extra Mana Per Tick (in war)
Self Spell Mana Cost Reduced by 1

#### Penalties:

-5% Max Population

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Magicians | (9, 0) |  |
Druids | (0, 10) |  |
Beastmasters | (4, 13) | 1,000gc | 7.25
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (2, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Miner's Mystique, Lightning Strike, Town Watch, Ghost Workers and Invisibility

#### War Doctrines

+1.5% **Defensive Military Efficiency**, scaling by +0.75% per province of this race in your kingdom (max +7.5%).

#### Unique - Arcane Overflow

Arcane energy surges beyond control, warping the very fabric of magic. Each strike not only harms but erodes the foundation of enemy rituals, unraveling their potency with every spell cast.

##### Passive Effect

(In War) Every successful offensive spell also reduces enemy ritual effectiveness by 0.15%.

### Gnome

#### Bonuses:

+10% Sabotage Damage
-25% Thief Losses
Train Thieves with Credits
Immune to Expose Thieves

#### Penalties:

+20% Combat Instant Spell Damage Received

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Quickblades | (11, 0) |  |
Pikemen | (0, 11) |  |
Golems | (13, 3) | 850gc | 6.0
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (2, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Quick Feet

#### War Doctrines

+5% **Birth rates**, scaling by +2.5% per province of this race in your kingdom (max +25%).

#### Unique - Cunning Assault

Your forces strike with calculated precision. Each successful attack may inspire a surge of cunning that enhances your thievery prowess for several days.

##### Passive Effect

Each successful attack will provide one of the following thievery boosts, which last for 6 days: +25% offensive thievery effectiveness, -25% thief losses, or +10% sabotage damage. All of these can be active at the same time.

### Halfling

#### Bonuses:

+10% Max Population
+25% Thievery Per Acre (TPA)
+1% Extra Stealth Per Tick

#### Penalties:

-20% Wizards Per Acre (Offensive Only)

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Strongarms | (9, 0) |  |
Slingers | (0, 10) |  |
Brutes | (6, 11) | 1,000gc | 6.75
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (2, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Invisibility

#### War Doctrines

+1% **Population**, scaling by +0.5% per province of this race in your kingdom (max +5%).

#### Unique - Overgrowth

Life surges beyond its bounds, spilling over in wild abundance. Homes overflow with people and every corner of the land bursts with growth untamed. The province thrives in a verdant tide of vitality.

##### Active Effect

Once activated, your maximum population increases by +25% for 5 days.

##### Cooldown

23 Utopian Days

##### Duration

3 Utopian Days

### Human

#### Bonuses:

+25% Income
-20% Military Training Cost
-20% Military Wages
Incite Riot Immunity

#### Penalties:

Self Spell Mana Cost Increased by 1

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Swordsmen | (10, 0) |  |
Archers | (0, 10) |  |
Knights | (13, 4) | 900gc | 6.25
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (2, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Tree of Gold

#### War Doctrines

+3% **Income**, scaling by +1.5% per province of this race in your kingdom (max +15%).

#### Unique - Civil Administration

Humans excel at organization and bureaucracy, running efficient prisoner work programs and maintaining well-regulated mercenary contracts. Their administrative prowess transforms captives into productive assets and ensures mercenary forces can be hired at favorable rates.

##### Passive Effect

Prisoners generate an additional 2.0 gold coins per tick. Mercenary costs are reduced by 40%.

### Orc

#### Bonuses:

+20% Battle Gains
-50% Draft Cost

#### Penalties:

-5% Defensive Military Efficiency

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Goblins | (11, 0) |  |
Trolls | (0, 10) |  |
Ogres | (14, 3) | 900gc | 6.25
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (2, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Bloodlust

#### War Doctrines

+3% **Enemy Casualties on defense**, scaling by +1.5% per province of this race in your kingdom (max +15%).

#### Unique - Generals Authority

When multiple experienced generals coordinate their efforts on the battlefield, their combined tactical brilliance transforms a victory into a massacre. The enemy military is outmaneuvered at every turn, suffering catastrophic casualties from the relentless, perfectly executed assault.

##### Passive Effect

When attacking with 2 or more generals, enemy military casualties are increased by +15%.

### Undead

#### Bonuses:

-100% Food Consumption
-40% Own casualities when attacking
-40% Own casualities when defending
Immune to the Plague

#### Penalties:

-15% Birth Rate

#### Military:

 | Off/Def | Cost | NW
--- | --- | --- | ---
Soldiers | (3, 0) |  |
Skeletons | (10, 0) |  |
Zombies | (0, 10) |  |
Ghouls | (13, 4) | 900gc | 6.25
Mercenaries | (8, 0) |  |
Prisoners | (8, 0) |  |
War Horses | (2, 0) |  |
Thieves |  | 500gc |  |

#### Spell Book:

Ghost Workers

#### War Doctrines

-4% **Own casualties on offense**, scaling by -2% per province of this race in your kingdom (max -20%).

#### Unique - Plaguebearers

The Undead carry pestilence in their very essence, spreading disease wherever their armies march. Each victorious assault leaves behind a trail of sickness, as plague spores cling to the living and corrupt all they touch.

##### Passive Effect

All successful attacks have a 33% chance to spread plague to the target province.

Personalities

### Cleric

#### Bonuses:

-15% Battle Losses
+15% Defensive Military Efficiency
-15% Combat Instant Spell Damage Received
-15% Damage Received on Massacre Attacks
-15% Sabotage Damage Received
Plague Immunity

#### Starting Bonuses:

+800 Starting Soldiers
+800 Starting Specialist training credits

#### Spell Book:

Salvation

#### Unique - Architect's Revenge

Dwarven architects take deep offense when their craftsmanship is questioned or threatened. Every attack on their stonework fuels their determination to demonstrate superiority, both in the impenetrable fortresses they raise and the devastating siege weapons they turn upon those foolish enough to challenge their mastery of stone and steel.

##### Passive Effect

Incoming Raze damage is reduced by 15%. Your Raze attacks destroy 20% additional buildings.

### General

#### Bonuses:

+1 Army generals
Elite gets +1 offensive strength
Offensive specialist gets +1 strength

#### Starting Bonuses:

+800 Starting Soldiers
+800 Starting Specialist training credits

#### Spell Book:

Righteous Aggressor

#### Unique - Undermining Assault

A calculated offensive aimed at more than just land — it fractures coordination and exposes gaps in the enemy's defenses. As confusion spreads, their ability to resist subterfuge crumbles.

##### Active Effect

Your next successful attack applies Coordinated Strike to the target for 4 days, reducing their Watch Tower thievery defense effectiveness by 15%. This effect cannot be used if Skybound Strike is active on your province.

##### Cooldown

23 Utopian Days

##### Duration

2 Utopian Days

### Heretic

#### Bonuses:

+50% Land Effect - Guilds
+10% Combat Instant Spell Damage
+10% Sabotage Damage
No thief losses on espionage operations

#### Starting Bonuses:

+400 Starting Thieves
+400 Starting Wizards

#### Spell Book:

Nightmare, Fools Gold and Mage's Fury

#### Unique - Silent Assault

When sabotage operations go wrong, expert infiltrators don't panic—they vanish. Through superior stealth and escape training, operatives slip away with minimal casualties, turning potential disasters into mere setbacks.

##### Passive Effect

50% fewer thievery losses when performing sabotage operations.

### Mystic

#### Bonuses:

+100% Land Effect - Guilds
+25% Wizards Per Acre (Offensive Only)
+1% Extra Mana Per Tick

#### Starting Bonuses:

+800 Starting Wizards

#### Spell Book:

Meteor Showers, Chastity and Pitfalls

#### Unique - Black Magic

The Necromancer's offensive spells carry a virulent curse that extends far beyond their primary target. Dark energy seeps into the enemy province, causing necrotic fallout that withers the living. Peasants fall ill and perish as the shadow of death lingers over the land.

##### Passive Effect

Successful offensive instant spells also kill 1% of the target's peasant population.

### Rogue

#### Bonuses:

+25% Thievery Per Acre (TPA) (Offensive Only)
+75% Thieves' Den Effectiveness
+1% Extra Stealth Per Tick
Access all Thievery Operations

#### Starting Bonuses:

+800 Starting Thieves

#### Spell Book:

Mystic Aura

#### Unique - Shadow Persistence

Rogues thrive in chaos and overcrowding, using the press of bodies and confusion of overpopulated streets to their advantage. Where others see disorder, the Rogue sees opportunity—operating freely even when the province strains under the weight of too many souls.

##### Passive Effect

You may perform thievery operations even while overpopulated.

### Sage

#### Bonuses:

-50% Losses on Learn Attacks

#### Starting Bonuses:

+800 Starting Soldiers
+10 Starting Scientists
+800 Starting Specialist training credits

#### Spell Book:

Scientific Insight and Fountain of Knowledge

#### Unique - Holy Inquisition

Paladins are zealous enforcers of divine order, wielding sacred authority to disrupt enemy intellectual progress. Each successful attack during War or Hostile relations applies divine judgment, temporarily suppressing enemy research capabilities and reducing their ability to generate new knowledge.

##### Passive Effect

Successful attacks in War or Hostile temporarily suppress 15% of the target's Science Effectiveness and reduce Book Generation by 20% for 6-8 ticks.

### Tactician

#### Bonuses:

-15% Attack Travel Time
+25% Specialist Training Credits
100% successful espionage operations at 2x stealth

#### Starting Bonuses:

+800 Starting Soldiers
+800 Starting Specialist training credits

#### Spell Book:

Illuminate Shadows

#### Unique - Dragon's Wrath

Tacticians turn adversity into opportunity, using precise strategies to retaliate against enemy dragons sent to weaken their province. With a Dragon's Wrath, their forces deal damage to the dragon during attacks, ensuring that even under siege, their resilience remains unmatched.

##### Passive Effect

When attacking with a dragon, 3% of your raw offense from units will also deal damage to the dragon.

### Warrior

#### Bonuses:

+15% Damage Inflicted on Massacre Attacks
+15% Offensive Military Efficiency

#### Starting Bonuses:

+800 Starting Soldiers
+800 Starting Specialist training credits

#### Spell Book:

Heroes Inspiration

#### Unique - Indomitable Spirit

Warriors embody unshakable resolve and unmatched discipline, drawing upon their indomitable spirit to rally their forces. When invoked, this ability inspires their armies to fight with heightened efficiency, turning the tide of battle in their favor.

##### Active Effect

Once activated Warriors gain 5% Military Efficiency for 6 days.

##### Cooldown

23 Utopian Days

##### Duration

6 Utopian Days

Here is the effects of all possible rituals.

Barrier | -20% Damage from Enemy Instant Magic & Thievery Operations, -20% Battle (Resource) Losses, -20% Massacre Damage
--- | ---
Benediction | +15% Building Efficiency, -20% Draft Costs, -20% Build Costs, +15% Birth Rate, +20% Draft Speed
Haste | -10% Attack Time, -25% Training Time, -25% Construction Time
Havoc | +25% Offensive WPA, +25% Offensive TPA, +15% Spell Damage, +15% Sabotage Damage
Onslaught | +10% Offensive Military Efficiency, +15% Enemy Military Casualties on Attacks
Stalwart | +5% Defensive Military Efficiency, -25% Military Casualties

Here are the effects of all possible dragons.

Emerald | +25% Military Casualties, -25% Combat Gains, destroys 1.0% of troops on arrival
--- | ---
Ruby | -10% Military Efficiency, +20% Military Wages, destroys 2.0% of military at home on arrival
Sapphire | -20% WPA and TPA, +15% Instant Spell and Sabotage Damage taken, kills 3% thieves and wizards on arrival
Topaz | -20% Building Efficiency, -25% Income, +20% Military Wages, destroys 10% of buildings on arrival

                            Copyright 2026 MUGA Gaming, LLC -

                            Contact Support
 Version: fdc5dd9

Report Content

You are about to report that the content below is in breach of the Code of Conduct. This is a serious allegation, which may result in disciplinary action against the player that uploaded it.**WARNING: Falsely reporting content is also considered an offense, and may result in your account being suspended, or worse.**

Report this
/shared/feedback/report_content/

---

# Part 3: Wiki Pages

> **PRIORITY: MEDIUM — Reliable for mechanics, formulas, and concepts. Unreliable for current-age specifics.**
> These are scraped wiki pages. They are valuable for game formulas, mechanics explanations, and strategic guides.
> However, they may reference races, personalities, abilities, or balance values from past ages.
> Do NOT use Part 3 as the source of truth for race/personality stats, unique abilities, or any data
> that changes between ages. For those, defer to Part 1 and Part 2.

## A Players Guide to Utopia

By Dan4GS. October 26, 2014 (Age 63 Changes included)
Originally published in Forums: http://forums.utopia-game.com/showthread.php?626895-A-Players-Guide-to-Utopia
Updated by Icebuckle for Age 89. January 1, 2021.

### Contents

- 1 Section I: What is the purpose of this guide?

- 2 Section II: What is Utopia and how do I get started?

- 3 Section III) My province is created, what do I do now?

3.1 Part A) Build your Buildings!
3.2 Part B) Get your military going!
3.3 Part C) Scientific Discoveries await!
3.4 Part D) Columbus discovered what?
3.5 Part E) You're Not Alone

- 4 Section IV) Ok, I've done what you said...what do I do now?

4.1 Part A) Activity is key
4.2 Part B) You can't stay small forever
4.3 Part C) It's about balance
4.4 Part D) DPA, OPA, TPA, WPA, pPA... what the heck is all this stuff?
4.5 Part E) Anything else you want to say?
4.6 F) Player Made Videos

### Section I: What is the purpose of this guide?

This guide has been written for those that are new to Utopia, specifically for those in my kingdom. Although the official Utopian Guide presents a lot of great info, I have found its organization somewhat lacking and its clarity on topics difficult for new players to understand. Hopefully, this guide will be a little more straightforward in helping new players to understand the game and how to play it effectively.
Also, keep in mind that this guide is purposefully simplistic. It is only an introduction to Utopia, not an advanced concepts guide. Please treat it as such. This is not a replacement for the official guide, but should be used as a supplement.

### Section II: What is Utopia and how do I get started?

Utopia is a turn based game, with turns progressing once every hour. In between the turns progressing, you can perform many actions, such as attacking, casting spells, or stealing resources from other provinces. Exploring new lands, building buildings, training your military, and researching books of science can all be ordered at any time and take differing lengths of time to complete, with the countdown to those resources becoming available processing every hour on the hour. These turns are known in game as "Ticks".
Utopia is a Medieval land divided into 40 different "Islands" consisting of 8 Kingdoms on each Island. Each Kingdom is composed of provinces, such as yours, coming together for the common good of the Kingdom. Kingdom's consist of anywhere from 1-25 provinces. The game is configured to automatically place new provinces in those kingdoms with less than 20 provinces so that all kingdoms have as close to 20 provinces as possible. Kingdoms can get to 25 by inviting other provinces to join their kingdom.
Utopia is played in "Ages" which last approximately three months each. At the end of the age, the scores are recorded and then all the provinces get reset so everyone starts all over again, and those that joined midway through the last round are given a chance to start on even footing.
Each kingdom chooses how to play the game as they see fit, as does each province. Generally, Kingdoms will pursue one of three things: Land (the total land of all the provinces in your kingdom), Honor (won by successful thief and mage ops, as well as successful attacks), or war wins.
Provinces will choose similar objectives for their own province depending on what they wish to accomplish. Generally speaking, provinces will try to either gain a high networth, gain Titles through honor, or seek to help their kingdom in whatever way possible. There are different ways of accomplishing these objectives, with three basic play styles and combinations of the three. Those three are: Attacker, Thief, and Mage.
Attackers rely upon a strong military to invade the lands of others to capture more land, to destroy their target's population or raze their buildings, or to plunder the wealth or knowledge of the province they are invading.
Thieves keep a strong enough military to prevent most invasions but focus on training sinister agents to do their bidding. Thieves are useful at gathering intelligence on enemy provinces, sabotaging the enemies magic effectiveness or destroying their buildings, and stealing resources, among other things.
Mages are similar to thieves in some ways, but focus on the dark magics. Mages can cast numerous beneficial spells on their own province to help with military protection, food production, or magical defense, among other things. They can also hurl large fireballs at enemies to massacre their peasants, send tornadoes through enemy provinces to destroy their buildings, or illuminate the thieves in another province to hamper their effectiveness, among many other abilities.
Most provinces will chose one primary function to focus on and one secondary function to help their kingdom with, while trying to keep enough balance in the third area so as not to make it a major weakness. For example, someone who wants to play as an attacker but also wants to dabble in black magic would be known as an A/m, with the first letter being capitalized to be the symbol of the main function of the province, while the second letter is lower case to show that the province is "minoring" in that function. An A/m would want a strong military for attack and defense and want to have enough mages to be able to successfully cast spells on most other provinces.
One popular combination is that of a T/m or M/t, since both tend to have more similar play styles than attackers and try to maximize the efficiency of the acres they do possess. You may choose any of the three functions as your focus, or you may try to focus on all...but be warned, being effective at all three functions requires a very skilled player and is close to impossible to succeed at!
There are certain races that lend themselves to specific functions, although it is theoretically possible to pursue any function as any race. For maximum efficiency, I'd recommend choosing a race that suits what you want to do in the game.
Here is a short breakdown of the races and their preferred functions:
**Avians**: Good at attacking with fast attack and fast training time. Because Avians fly into combat, they cannot use war horses or build stables. To make up for the lack of war horses, their offensive specialists have 12 attack instead of the typical 10. Primary role: Attacker; Secondary role: Thief
**Dark Elves**: Dark Elves can use offensive spells with no cost with mana being the main limitation. Affected by slightly lower building efficiency. Primary role: Mage; Secondary role: Thief or attacker
**Dwarves**: All rounder with a focus on buildings. Dwarves have increased building efficiency and lower construction costs, so they are able to change up their builds depending on the situation. The downside a lower birth rate, so they re-populate slower than other races. Primary role: Attacker; Secondary role: Mage or Thief
**Elves**: Increased magic effectiveness and double rune production, making them very suitable as mages. They have strong defense with defensive specialists having 12 points rather than the typical 10 points. To maintain their military, they have to pay more wages. Primary role: Mage; Secondary role: Thief or attacker
**Faeries**: Great thieves thanks to their additional thievery effectiveness. They are also able to defend better with lowered defensive military casualties, making them a less likely target for the opposing armies. Additionally, although faeries do not have any magic bonuses, they have access to all racial spells. Faeries pay for this with a slight limitation on their population size. Primary role: Thief or Mage;
**Gnomes**: All rounder with increased population size, increased birth rate, and less food consumption. Gnomes is the only race with no negative modifiers. Primary role: Attacker, Thief, or Mage;
**Humans**: Attacker with a focus on money. Humans have increased income and increased credits gained during combat. Strong attack focused elite. They make poorer mages due to their additional rune cost. Primary role: Attacker; Secondary role: Thief
**Orcs**: Bred for attack with additional enemy casualties and very offensive oriented elites, though they take more damage from mages and thieves. Primary role: Attacker;
**Undead**: Being undead certainly has its advantages, as this race loses less troops when attacking and part of the troops lost immediately become soldiers again that can be trained. The Undead also do not require food for sustenance, allowing would be farms to be converted into other buildings. Further, the Undead are the only race that actively spreads the plague, and are also the only ones immune to it. Undead are very attack oriented with strong offensive elites. Their limitation is that they cannot build any homes or hospitals. Primary role: Attacker;
After you have chosen which race you would like to play, you will also need to choose a personality to give you additional benefits. Here is a quick breakdown of personalities:
**The Cleric**: The Cleric is able to heal their troops during combat, resulting in 30% fewer casualties. They can also cast support spells on kingdom members. Generally this personality is best for an Attacker/mage, with a focus on attacking and then using runes to cast support spells for the kingdom.
**The Heretic**: The Heretic increases wizard production and makes it so that there will be less thieves lost. Additionally, more damage from spells and operations. A perfect personality for Thief + Mage play.
**The Mystic**: The Mystic is the only personality with access to the spell Meteor Showers. Guilds are doubly effective and they have an increase in mana recovery, allowing for more spells to be cast. The Mystic is a good choice for anyone wishing to play a Mage as their primary play style.
**The Raider**: The Raider is effective at plundering and is the only personality that can use specialist credits to train thieves. The raider also does not need to build Stables or Dungeons as each acre will automatically house War Horses and Prisoners. The Raider is a good choice for Attacker/thief play.
**The Rogue**: The Rogue focuses on thievery and ops and grants the ability to conduct more thievery ops than one otherwise would be able to with additional stealth recovery. Rogues are the only ones able to perform the following ops: Assassinate Wizards, Greater Arson, and Propaganda. The rogue is a good choice for anyone wishing to play a Thief as their primary play style.
**The Tactician**: The Tactician benefits from faster attack times and accurate intel with a small number of thieves. The tactician is a nice pairing with Avian Attackers for very quick attacks (add barracks for even more advantage to attack times) or any other dedicated Attacker. This is not a great choice for those that do not plan to attack often.
**The War Hero**: The War Hero gets additional combat gains and additional conversion into elites. They also benefit from less honor loss during combat. The War Hero is a strong personality for Attackers, especially being the only one with +3 elite bonuses (2 for offense, 1 for defense).
**The Warrior**: The warrior benefits from an increase in offensive efficiency and additional prisoner and mercenary strength. The Warrior also gets a significant on mercenaries. The Warrior is a good choice an Attacker, especially one paired with money to leverage the mercenaries.
For more numbers on each race and personality, see these links: Race & Personality
Now that you know the basic function of each race and personality, begin by deciding what play style you want to play, then choose races and personalities that you believe make the best combination for your chosen play style. After that, create your province and see what kingdom you joined!
For additional ideas on choosing a play style, check out this guide for more considerations: Beginner's Guide to Choosing Race and Personalities.

### Section III) My province is created, what do I do now?

#### Part A) Build your Buildings!

So you've just logged in for the first time and you see a basic synopsis of your province, known as the "Throne Room". This screen displays how much land you have, how many GC (Gold coins) you possess, how many military and thief units you have, along with many other bits of information. Below the box with all the info is a newsreel where new events will be posted as they occur. When you are away and things are happening to your province, a detailed list of all those events will be waiting in your newsreel when you return. After the first time those events are displayed, the newsreel hides them unless you click on "See all news".
Above the box might be a message from the King or Queen of your kingdom, with basic directions or goals for everyone in the kingdom to follow. But enough with the throne room, you won't get anything done sitting here...it's time to build some buildings!
Buildings can be broken down into several different types:

- Civil Buildings.

- Military Buildings

- Thievery and Mystic Buildings

- Science Buildings

It is best not to build some of every type of building, rather, focus on building more of several type of buildings you think would best benefit you.
Buildings can also be broken down by a different category:

- Flat rate

- Capacity

- Percentage based

Flat rate buildings give you a certain amount of the resource they generate no matter how much of your land is dedicated to that specific building.
Capacity buildings fill up to their listed capacity and are not effected by building efficiency.
Percentage based buildings give your province a bonus depending on what percentage of your total land is dedicated to that type of building. For instance, Forts provide 1.5% extra defense for every 1% of your land that is built as Forts. Thus, if you were to have 1000 Acres and 100 Forts, you have 10% of your land as Forts and receive a 15% increase to your total defense! (This number is calculated before diminishing returns and Building Efficiency {abbreviated BE}, which can skew that number.) Keep in mind that some buildings are not affected by your Building Efficiency (more on BE later).
Therefore, your first goal should be to figure out what buildings you want and how much of each building you'd like to have. There are several buildings that every province should have, and those are as follows:

- Farms (unless Undead)

- Guilds (to produce wizards and cast spells on your province)

- Towers (to generate runes necessary to cast those spells)

In the beginning, 10% of your land should be dedicated to farms to provide enough food for all your peasants and military. Guilds and towers can vary depending on what you'd like to focus on, but generally speaking 10% guilds and 5% towers is good enough to cast spells on yourself.
Here is a quick breakdown of the other buildings by type:
**Civil Buildings**

- Homes: Increases your birthrates and houses more people than other buildings. This is the only building that does not provide any jobs (which can help your BE). Capacity building and Percentage based.

- Farms: Generates food. Flat rate.

- Mills: Decreases exploration and building costs. Percentage based.

- Banks: Generates GC every day and increases your income by a percentage. Flat rate and Percentage based.

**Military Buildings**

- Training Grounds: Increases your offensive military efficiency. Percentage based.

- Armories: Decreases the cost of training your military. Percentage based.

- Forts: Increases your defensive military efficiency. Percentage based.

- Barracks: Decreases the time required for your troops to attack. Percentage based.

- Guard stations: Decreases the amount of land or resources lost when you suffer an attack. Does not increase military efficiency. Percentage based.

- Hospitals: Decreases the amount of troops lost during combat and has a chance to cure the plague. Percentage based.

- Stables: Produces war horses to increase your offensive power. Capacity building.

- Dungeons: Houses enemy prisoners of war captured during an attack. Capacity building.

**Thievery and Mystic Buildings**

- Guilds: Trains wizards. Flat rate

- Towers: Produces runes, which are used to cast spells. Flat rate.

- Thieves Dens: Lower losses when you get caught thieving and increased thieving efficiency. Percentage based.

- Watchtowers: Protection against thieves. Percentage based.

**Science Buildings**

- Libraries: Increases your science efficiency. This building is not affected by BE. Percentage based.

- Schools: Decreases science costs and protects your books of learning from would be invaders. Percentage based.

- Barren Land: Although not a building, you'll have some lying around at times. Barren land does house some people and also provides a small amount of food. Generally speaking, you should build up barren land as soon as you are able.

What buildings you build is entirely up to you, but remember, the more types of buildings you produce, the less effect each will have. Most players believe it is better to choose several types of buildings and build more of them than have a small percentage of many types of buildings.
Here are a couple samples of building strategies, starting with **Attacker**:

- 10% Homes

- 10% Farms (Food)

- 12% Training Grounds (Better attack power)

- 10% Armories (Cheaper troops)

- 10% Hospitals

- 10% Barracks (Faster attack time)

- 10% Guilds (Got to have some wizards to cast spells)

- 5% Towers (Need runes to cast spells)

- 10% Stables (To house your warhorses and increase offense)

- 3% Dungeons (House your prisoners of war, which can then be used to increase your offense)

- 10% Watchtowers (To decrease your susceptibility to thieves)

While there are many different possible building strategies, this one covers most of the basic needs of your province.
Here is one for a **Thief**:

- 10% Homes

- 10% Farms (Food)

- 10% Banks (Additional money)

- 15% Guilds (If you're a thief, you'll probably want some magic ability too)

- 10% Towers (To cast spells)

- 20% Thieves Dens (Reduce thief losses and increase effectiveness)

- 10% Forts (Increased defense)

- 15% Libraries (Increased science = more efficient with the acres you have)

And finally, here is one for a **Mage**:

- 10% Homes

- 10% Farms (Food)

- 10% Banks (Additional money)

- 20% Guilds (You'll need lots of wizards if you want to cast spells on everyone)

- 15% Towers (To cast lots of spells)

- 10% Thieves Dens or Watchtowers (Reduce thief losses and increase effectiveness or prevent thieves from harming your wizards)

- 10% Forts (Increased defense)

- 15% Libraries (Increased science=more efficient with the acres you have)

Now these are some basic strategies and I would encourage you to come up with your own. Look at the numbers of each building, found here: Growth. From there, create your own building strategy and take the time to do the math to stick to it.

#### Part B) Get your military going!

Now you've finished with your building strategy and you're ready to move on. Time to go check out the military. Once you click on the "Military" link on the left side of the screen, you'll go to a menu with a couple of boxes. The top box allows you to set your draft rate and wage rate. During protection, your wage rate is set at 100% and cannot be changed. After you leave protection, you can set your wage rate to 200% to increase your military efficiency (both offense and defense) to 107.5% of normal efficiency. You can also choose to drop your wage rate as low as 20% of normal, but your men will be much less efficient.
Your draft rate determines what final percentage of your total population will be in the military. It should be noted that Thieves are counted as "being in the military" even though they cannot attack or defend during military engagements. Most provinces will have more than half of their total population in the military, while some provinces choose to go much higher. You'll also notice that you can change the rate at which peasants are drafted into your military. There are four settings here, ranging from slow to fast, with the cost per soldiers increasing the faster you draft soldiers.
Below that first box is where you see how many current troops you have. There are four basic military units:

- Soldiers

- Offensive Specialists

- Defensive Specialists

- Elite Troops.

The names are different for every race, with the exception of soldiers, which are called the same everywhere.
Soldiers have basic capability of both offense and defense, but are very weak at both. Soldiers are drafted from the peasantry and can then be trained into more advance troops. Soldiers typically have 2 offensive and 2 defensive point.
Offensive specialists are useful only for offensive endeavors and do not participate in defensive battles. They are fairly cheap to train and typically have 10 offensive points and 0 defensive points.
Defensive specialists are useful only for defensive purposes and cannot be sent out on attacks. They costs the same as offensive specialists and typically have 10 defensive points and 0 offensive points.
Elites troops are more costly than specialists but can participate in both offensive and defensive endeavors. Elite troops also add more networth to your province than specialists. Elites have different offensive and defensive points and costs different amounts depending on what Race and Personality you play.
When you first start a province, you will be given a set amount of soldiers. If you have constructed armories, do not train these soldiers yet; instead, wait for the armories to be constructed to benefit from the decreased costs of training troops. Also, you may wish to use those soldiers to explore instead of training them up right away. The choice is yours, just make sure you set your draft rate to draft new soldiers into your army!

#### Part C) Scientific Discoveries await!

You've finished building and inspecting the troops and it's time to see how your scientific research is being handled. You'll notice a similar screen to the "Military" screen with some similar functions.
Scientists generate books that can then be allocated to a specific Science Type. At the top of the page, you can see **Current scientist generation**. This is automatic and can speed up by building more Laboratories.
You can then choose the **Category for Next Scientist** to determine where the scientist generated will go when it is at 100%. Universities can help increase the rate of books production in a Science Category: **Economy**, **Military**, or **Arcane Arts**.
Under **Current Effects of Science**, just spend the number of books available into the science that you want to spend on. Each Science Type will have the bonuses listed next to it.
You should think about what type of province you are playing and assign your research as such; there is no point in someone who will never attack researching Tactics and Siege, as both of them are only useful during attacks.
For more information on the sciences, check out Science Formulas.

#### Part D) Columbus discovered what?

You've done the basic things required to get your province up and running, but you'll quickly run out of available acres to build on unless you add more. There are only a few ways to add acres:

- Exploration,

- Military endeavors (via attacks like a Traditional March)

- Magic (via the spell, Paradise)

During protection, the only way to add acres is through exploration, which is also the most cost effective way when a province is small. Exploration requires a certain amount of soldiers per acre discovered as well as GC to fund the expedition. Note that specialists and elites cannot be used to explore, only soldiers. It is generally a good idea to explore for more acres during protection, just don't explore too much and neglect your military lest you be attacked after protection ends and lose what you spent on exploring!
After protection ends, exploring is still usually the most cost effective way to grow. You can explore for as much as you have soldiers and GC to fund, provided your province has more unexplored acres. Every province has a "Pool" of acres that can be explored. This pool grows a bit every day.
Because Protection is only 24 hours, the recommendation is to explore no more than 50 acres and instead, focus on getting everything ready in Growth and Military. If you so happen to land in a Kingdom during war, your protection period will be 72 hours instead. In this case, exploring a little more is fine, but the focus should be to build out your military so that you are ready to help attack, cast spells, or steal.

#### Part E) You're Not Alone

Now that you've sent some soldiers out to discover new territory to bring into your province and you're ready to meet the neighbors. **This might be the most important part of the game**, as those in your kingdom will be your closest allies going forward. Check in at the forums and say hello; your neighbors are sure to want to greet you and help you with any questions you may have. It is here in the forums that you and your kingdom mates can discuss strategy, goals, war, peace, request aid, or discuss non-utopian topics. Utopia, at its heart, is about human interaction, and if you do not visit the forums and talk to those in your kingdom, you're missing a large part of the game.
One last part of being in the kingdom is voting for the King or Queen (also known as the Monarch). To vote, click on the "Politics" tab on the left side of the screen. Usually it's best to vote for whoever is already King or Queen, but if there is not established ruler, there is probably a couple of provinces in the forums jostling for the position. Check the forums and read what each has to say and vote for the one you think would make a better ruler. Keep in mind that the King or Queen should not necessarily be the biggest province, but should be one that knows the game and is dedicated to putting the Kingdom before themselves. Once you've decided who to vote for, go vote and support your chosen leader!

### Section IV) Ok, I've done what you said...what do I do now?

#### Part A) Activity is key

Congratulations! You made it through your first login on Utopia! Now you'll have to keep checking back on your province to continue exploring, training your military, researching more books of science, and coordinating with your kingdom mates. How often you choose to log in is up to you, but it is recommended you log in several times a day. If you do not log in for a period of 48 hours, your province will be shown as inactive to your Monarch and he or she might destroy your province, so make sure to log in at least once a day if not more!
During war time, it is recommended you log in much more often. Due to the nature of wars, the more active you can be logging in and running ops on the enemy or attacking him with your armies, the more you'll help your kingdom and the likelier you are to win the war.

#### Part B) You can't stay small forever

The title of this part is actually completely false. You could stay at your original size as long as you wanted and no one attacked you, but you probably shouldn't. The more acres you have, the more money you can earn, the larger the army you can field, the more thieves and wizards you can train, and the more you can contribute to your kingdom.
Utopia gives every province 10 acres of land per day, for free. There is no way to NOT get the 10 free acres of land. You might as well use it as part of a greater growth plan. If, figuring the age lasts for 90 days (approximately 3 months) and you explore only 30 acres a day (and get the free 10 acres to bring you to 40 acres/day), you'll end the round with about 3800 acres, which is nothing to scoff at. It is quite possible to explore 30 acres/day and keep a sufficient defense plus be able to focus on whatever strategy you have chosen. Of course, that does not mean you should limit yourself to 30 acres/day if you want to grow more. Conversely, sometimes it is best not to grow that much. It is important to stay within range of your kingdom teammates if there are war plans on the horizon.
All this must be weighed against several things:

- The bigger you are, the more resources are at your control. You can finance dragons easier when you're bigger or slay dragons quicker with more soldiers at your command. Having more acres allows you to field a larger army and gives you more money to invest in research, although as mentioned previously, you'll need a lot more books to keep the same rate of return as a smaller province.

- Military attack gains are dependent on the networth and land size of both the attacker and defender. For best results, you'll want to attack someone close to you in networth, and you want to have less acreage than they do. Thievery and magic operations work similarly; the greater the disparity in networth, the higher the chance of failing the op.

- The kingdom needs to determine what objective it is trying to accomplish that age. If the kingdom is trying to gain networth, a larger province will be able to achieve a much higher networth than a small province. If the kingdom is playing for honor, it might be more effective to stay smaller and focus on efficiency through science. If the kingdom is playing for war wins, the kingdom will probably need a good mix of province sizes to effectively counter what the opposing kingdom is doing.

- The higher the networth of the kingdom, the more intimidating other provinces might find it, and thus less are willing to take the risk of attacking into that kingdom. This works to protect all the provinces in the kingdom, but only if that kingdom is bigger than the kingdom from which the attacker is attacking.

- More often than not, highly active and skilled kingdoms wind up with larger networths and more acres. Thus, a highly skilled and active kingdom might choose to remain smaller to fight less active and less experienced kingdoms to achieve quicker war wins. The downside of this is that the kingdom as a whole would not be able to repel attacks from significantly larger kingdoms.

As mentioned previously, there are three ways to grow: Exploring, Attacking, and Magic. The first two have been covered to some degree. Those adept at the magical arts can choose to cast the Paradise spell while not in war to create several acres of new land without sending out soldiers to explore. This spell is costly and difficult to succeed at, but an accomplished mage should be able to have little difficulty with it. The second option, during war time, is to cast Land Lust, which will steal several acres from the target province and give it to the casting province. Again, this is a very difficult and costly spell to cast.

#### Part C) It's about balance

At some point you'll notice that you've got a certain percentage of your land dedicated to one type of building, but when you go to your Internal Affairs advisor, you'll see that you're not getting the return you expected from that building. There are two reasons for that: Building Efficiency (BE) and diminishing returns. Let's talk about these and other balance issues you'll likely encounter during your time in Utopia.
Building efficiency is how efficient your buildings are. Each completed building houses 25 people and also provides 25 jobs. Peasants in Utopia work harder than you do in real life, and are thus able to fill 1 and 1/2 jobs each. It's pretty easy to figure out, then, that if you have built up all of your acres and do not have any homes, and have 50% of your population in the military, you will not have enough peasants to fill all jobs.
Don't worry, there are modifiers to this equation. Homes increase your population without adding jobs, which can help alleviate some of these problems. Gaining Titles through honor grants an increase in population limits, and humans have an increase in population limit naturally. Also, researching Books of Housing will increase the overall capacity of your buildings, allowing you to field a larger peasantry. Even with all those modifiers, though, you're not likely to fill every available job.
But don't worry, building efficiency is not determined simply by your total peasants divided by number of jobs. If that were the case, it'd be impossible to field a decent army and maintain building efficiency. Utopian peasants work 1 and 1/2 jobs each, so you only need 67% of total jobs to be filled by peasants in order for every job to be worked. If less than 67% of your total jobs are worked, your building efficiency will drop depending on how many additional unfilled jobs you have. It should also be noted that Dwarves get a bonus to building efficiency, Books of Tools can be researched to improve building efficiency, and there are other more complicated factors such as dragons and stances that can also affect building efficiency.
The last thing you should know about BE is that the rate won't drop instantaneously. If you suddenly drop a large amount of peasants due to kidnappings in your province or fireballs sent do destroy your peasants, instead of your BE dropping immediately to the levels it should be, the level is dropped gradually until it reaches the point it should be mathematically. Likewise, if you recover many peasants quickly or add to your population in a hurry, your building efficiency will not raise as high as it should be instantaneously; rather your BE will improve a little every "Tick" until it reaches its resting point.
Now that you understand BE, there is one final factor in understanding why your province doesn't get as much out of your buildings as it should, and that factor is diminishing returns. Simply, the higher percentage of a certain type of building you have, the less benefit each additional 1% will give to you. Therefore, the first 10% of your land you dedicate to a percentage based building will be more effective than the next 10%, and so on. This does not affect flat rate buildings, which have a fixed production no matter what percentage of your land is dedicated to that type of building.
Creating an effective province is more than just about balancing your peasants and jobs. You also need to worry about having a large military, training thieves and wizards, and having enough soldiers to explore, if that is how you choose to grow. The larger the military you field, the less peasants will be available to work jobs and help your buildings attain maximum efficiency. Only peasants and prisoners of war work jobs and create income through taxation (which you cannot adjust), so the larger the military you have, the less gold you'll receive per tick.
But if you have too small of an army, your peasants will be defenseless and invading armies will steal your lands. Finding the right balance point is complicated and is highly province specific, as some provinces will sacrifice economy for military strength, or vice versa.
From the percentages provided above, we now know that you need to fill about 67% of your jobs to attain maximum BE, assuming no homes or other modifiers. It would make sense, then, to have at least 33% of your total population in the military. However, if you build some homes or have other factors that increase your total population limit, such as science, honor, or racial bonuses, you can safely increase your draft rate without harming building efficiency.
It should also be noted that it is often worth the cost of sacrificing BE to increase your overall military, which consists of military specific units and thieves. Wizards are not part of your military, but also are not peasants and do not work jobs or provide income. The percentage of your total population dedicated to non-peasant roles is entirely up to you, and finding the right balance between working peasants, military, and wizards is one of the keys to the game. During wartime, especially, it is often more important to have a larger military, more thieves, and more wizards, than it is during peacetime. This rate should be adjusted as often as you need it to be, and can sometimes change every day or several times per day, depending on the current needs of your province.

#### Part D) DPA, OPA, TPA, WPA, pPA... what the heck is all this stuff?

There are many acronyms in Utopia, several of which are key to figuring out the correct balance point for your province. All of the above acronyms are something Per Acre. Thus, DPA is Defense Per Acre, OPA is Offense Per Acre, TPA is Thieves Per Acre, WPA is Wizards Per Acre, and pPA is peasants Per Acre. There are plenty of other acronyms that are useful in the game, but for now we'll discuss these ones.
To calculate any of these acronyms, the math is pretty simple. For example, to calculate DPA, simply take your total number of defensive points and divide that number by your total number of acres. Defensive points can be manually calculated by multiplying soldiers by 1, defensive specialists by 4 (5 for Elves), and Elites by whatever your racial elite has for defensive points. Add those three categories together and you'll come up with your total defense. Now divide that by your acres, and voila, you now know your raw DPA! Your final DPA can include several modifiers, such as Forts, stance, protection spells, and wage rate. When you calculate all those modifiers, you come up with your total DPA. Of course, Utopia has made these calculations part of the game so you need not worry about doing all the math yourself. Instead, simply check in at your military adviser and he'll tell you your total OPA and DPA.
TPA and WPA are very important numbers because these determine how successful you are at thievery ops and spells. When attempting to thieve or cast a spell on another province, the winner will largely be determined by who has a higher TPA or WPA. Of course, different thief ops and spells have differing degrees of difficulty, and the harder the op or spell is, the greater disparity you'll need between your TPA or WPA over your target's TPA or WPA. There are also other modifiers, such as the overall networth of each province. Provinces with significant disparities in networth will have a harder time thieving or casting spells on each other than those of similar networths, assuming TPA and WPA hasn't changed.
Again, though, we now run into the balance issue. While it may be great to have 500 acres and have 5 TPA, that will limit your total number of thieves to 2500. The higher percentage of your thieves you send on any specific op, the greater chance they have of failing (due to oversaturation). Send fewer thieves, though, and your op may be successful but will not destroy or steal as much when you send more thieves. Growing larger allows you to field a larger network of thieves, and if you are 1500 acres with 5 TPA, you now have 7500 thieves at your disposal. Now you can send 2500 thieves but still only be sending 1/3 of your total TPA, increasing your chance at successfully completing the op (due to lower % of your thieves sent) and still destroy or steal a significant amount of your target's resources.
Keep in mind that more acres means more science is required to keep the same efficiency that a smaller province has with less science, and the more acres you have, the higher the chance an attacker will look at your acres and wish to attack and steal some of your acres for themselves. Of course, having more acres also allows you to have a larger economy and draft more soldiers during times of war, which will help combat any dragons sent over during the course of the war. It all comes back to balancing your province at the size and rates you think are most effective for your desired goals.
How much defense is a good defense, and how much offense is a good offense? While DPA and OPA are important numbers to give you a measuring point, there is no "right" answer for these questions. The answer is simply "As much as you can afford". Again, it's about balancing your province. The Official Utopian Guide has a article about some basic numbers to aim for depending on what part of the round you're currently in, and can be found here: It should be noted, however, that in Utopia the best defense (for attackers) is a big offense!
No matter what your goal is for the game, every province must have enough defense to protect itself from its most likely attackers, that being out of war vultures looking to steal some easy acres. There is no way to defend against every player in the game as there are just too many other players and there will always be someone bigger. During a war, nearly everyone will be attacked regardless of how much defense you have. The objective, then, of defense is to have enough to prevent multiples attacks by larger provinces and prevent others from sending small amounts of offense to capture large amounts of land.
For attackers, this balance is harder to achieve because you'll also need a substantial offense in order to capture acres from similarly sized provinces. Just as thieves and wizards are more effective against provinces of similar networth, attackers gain significantly more by attacking provinces close to them in networth. It may be obvious, but the more land a province has, the more a successful attack will capture. Therefore, the optimal target for attackers is one with more acres and slightly less networth. Attacking a province less than 80% of your networth will yield significantly less acres, as will attacking a province greater than 120% of your networth.
In order to launch successful military assaults, attackers will need to field a large offense, which can be measured in OPA. As with defense, you can never have enough offense. OPA is a less important number than DPA in some cases, as the larger a province is, the more potential targets there are, even if they yield less land or resources during an attack. This is never more pronounced than during a war, and is the reason attackers want to have large offense. The larger an attacker is, the larger an offense they can field.
There are also many more bonuses for attackers than there are for defenders. Training grounds provide a bonus to offensive military efficiency (OME), war horses add one point of offense per horse, prisoners of war can be sent back into combat to fight for you and add 3 offensive points per prisoner, and mercenaries can be purchased to fight for you, also adding 3 offensive points per mercenary. Further, there are several spells which can increase offensive attack power, such as Aggression (helping soldiers) and Fanaticism (increasing OME). The last modifier is your wage rate, which increases (or decreases) both offensive and defensive military efficiency. Combined all together, a province can significantly increase their available offense by utilizing all available ways of increasing their offense. Not all races have access to those spells, so if you want to play as an attacker, one factor would be considering which race has access to the spell you would like.
Defensively, the list of potential bonuses is a little smaller. As with offense, your wage rate can increase your efficiency. Forts also increase your defensive efficiency, and there are two spells which can help you defend your lands. Minor and Greater Protection both offer a small bonus to defending your lands, with the percentage bonus being the same for both spells but the length the spell is active for being the only difference. Town Watch is the only other way to increase your defense, and will utilize your peasants to fight in defense of your lands. Keep in mind, though, that if you cast Town Watch and are attacked, your peasants will also die in the conflict, which can hamper your economy.
The last acronym I have mentioned is pPA (peasants Per Acre). This may be the least important of the statistics, but when spying on another province can be an indication of how much science they have. Since housing science is so important, and it is likely most provinces will have spent some time researching books of housing, the higher the peasants per acre a province has, the more likely they are to have science. This can be useful for attackers looking to find target to use a Learn Attack on, which captures some of the science of the target province. For more on finding good provinces for Learn Attacks, see this article in the official Utopian Guide: http://wiki.utopia-game.com/index.ph..._Learn_Targets

#### Part E) Anything else you want to say?

That just about wraps up the basics of the game, although there are more advanced concepts which the guide will eventually cover. The important things to remember is that Utopia is a game about people, and how you interact with your kingdom will go a long way towards determining your success as a province and the enjoyment you get from the game.
Utopia is not a sprint; rather, it's a marathon. Building a great province is much less about how many times you can log in during a day, but rather about consistently logging in every day to tend to your province and help it grow as you see fit. Logging in multiple times one day then waiting several days before your next log in will lead to a dysfunctional province; it is better to log in fewer times but more consistently and grow your province over time.
Remember that Utopia is at its core, a game of kingdoms against each other, more so than individual provinces against each other. Don't be afraid to sacrifice personal ambitions and achievements for the good of the kingdom and be willing to change play styles if the kingdom needs you to and you feel you have the ability to play different styles. You might end up enjoying a style you did not think you'd enjoy!

#### F) Player Made Videos

I did not make these and all credit goes to their creator, who did a fantastic job!

- Creating a province: http://www.youtube.com/watch?v=QzsFh58X-io

- Basics of Utopia: http://www.youtube.com/watch?v=kBk90x5z4GY

## Ages

Each game of Utopia is broken up into separate Ages.
Each Age is unique, because every Age has different rules (game mechanics and races abilities), it is unwritten rule, that something changes. So new Age is not restart only.
An Age is usually 3 months long.
After the Age ends the game servers are reset and each province reverts back to its starting size in a new location.
Details: Utopia Time

### Historical Facts

**Races**:

- First born races were Dwarf, Elf, Faery, Human and Orc. Just 5.

- At Third Age also born Avians and Halflings. 7 together.

- At Sixth Age appeared Undead race. 8 together.

- At the beginning of Age of Bravery extinct Avians, Halflings, Undeads and Faerys. Instead them were born Gnomes and Dark Elves. 6 together.

- At the Age of Rebirth Undeads were reborn. 7 together.

- At the next age (Age of Light) Undeads extincted once more. But Avians were resurrect. 7 together.

- At the next age (Age of Justice) Halflings also ressurect. 8 together.

- At the anniversary Age (Age of Resurrection) Dark Elves and Gnomes extinct, Undead and Faeries return. 8 together.

- So, Dwarf, Elf, Human and Orc live at Utopian World of Legends forever all ages.

- Last born races were Gnomes and Dark Elves - appeared only at 36th age. Both of them lives 14 ages only. Less than anyone else.

- Undead appeared thrice and extincted twice - more than anyone else.

**Personalities**:

- The significance Personalities before the Era of Mystery was unknown, so Personalities didn't exist before

- At the Era of Mystery anyone could choose one of next Personalities: Merchant, Shepherd, Sage, Rogue, Mystic, War Hero, Warrior, General and Freak. 9 together.

- At the Age of Bravery The General was eliminated. 8 together.

- At the Age of the Scholar Freak was eliminated too. But the Artisan appeared. 8 together.

- At the Age of Rebirth Artisan was gone. Instead him Cleric appeared. 8 together.

- Cleric survived till Age of Light. But Artisan return. 8 together.

- Next Age (Age of Distinction) War Hero was upgraded to Tactician.

- At anniversary Age (Age of Resurrection) Cleric was reappeared, Artisan gone.

- At Call to Arms War Hero became as a new personality, but Shepherd gone.

- War Hero, Artisan and Cleric reappeared.

- At the Age of Heresy, Merchant was eliminated and Heretic appeared.

**Islands**:

- At the First Generation at the World of Legend existed 17 islands.

- Since beginning Islands was divided by Ocean. Nobody without boats could attack any province from outside Island.

- At the next Age already existed 25 islands.

- Next, Third Age  have 35 islands

- At the Fifth age number of islands grow till 40.

- Next Age World of Legends has 45 islands.

- Finally, at Seventh Age were 49 islands

- This Seventh Age Ocean was already dried, so only rivers divide islands. Shipbuilding was forgotten. Horses become more useful than boats.

- Far far away, at the Age of Kings number of islands was cut to 40.

- During the Isles of Legion the number of islands was cut to 20

**Science**:

- Since beginning existed Alchemy, Tools, Housing, Food, The Art of War, Crime & Deceit, Channelling

- At the Sixth Age was added Medicine study.

- Medicine studied only 3 ages till Age of Chaos, next Renaissance Age this discipline was forbidden forever

- At Era of Mystery were contrived Libraries, but they add Science into random category

- At the Age of Valour were discovered that exist decay of science each Utopian day. Universities begin to lower decay

- At the Age of the People Libraries becomes more effective and produce free science points

- At the Revolution discover, that Universities are the reason of science decay, so Universities become forbidden

- At the Age of Courage The Art of War was shortened to Military

- At the Age of Kings everybody understand that science points is just books

- At Age of the Scholar became impossible to direct money for certain research. New system : automatically investigate research into books. Then books were studied and allocated into category.

- Since New Code, Age of Change Crime & Deceit was shortened to Crime

- Learn Attack and Schools exist forever

**Nobility**:

- There is unclear if Nobility exist First Generation and Second Age

- At least since Third Age fame was in Utopia

- At Renaissance Age fame was modernized to Honor

- Finally at Age of Nobility Titles were discovered and List of Titles at once assumed modern view

- Benefits of Honor/Fame was changed too frequently

**Combat and Military**:

- First known attacks since beginning were Missionary, Traditional March, Raze, Plunder and Learn

- World of Legends always have Elites units

- At First Generation there were Solders(1/1), Offensive specialists(3/0) and Defensive specialists(0/3)

- At the Era of Magic was discovered new type of combat - Massacre

- Next age (Era of Mystery) Conquest was discovered. But Missionary become totally inaccessible

- Next Age (Era of Strife) units become more powerful: Solders(2/2), Offensive specialists(4/0) and Defensive specialists(0/4)

- At the Age of Conquerors Solders(1/1) become powerless

- At the Revolution Ambush become available

- Next Age (Age of Glory) Offensive specialists(5/0) and Defensive specialists(0/5) attack better

**Relations**:

- It is unclear how War looks at early Ages. We know they existed.

- We know exactly that at least since 5th Age were Multi-Kingdom Wars. It was needed just to declare a War to any Kingdom (any size). Other participants could join the War.

- We don't know if multi-kingdoms were limited by maximum or not. At least at 11th Age (A. of Nobility) War was limited to 5 participants (also limited size).

- We have poor information about Peace. Peace existed at least from 11th Age, and there is evidence it exists since beginning.

- Peace was looked like Peaceful Stance, you declare intention, but only for one/several Kingdoms and have benefits from this.

- If both Kingdom was in Peace, both of them have Binding Peace, which has same effect as Non-Aggression Pact now-days

- At the Age of Valour rules changes. Multi-Kingdoms Wars were abolished.

- Since that Age (Age of Valour) Kingdom could declare a new relation - Hostile (only 3 Hostile per one time at one Kingdom was permitted). War become automatically if both Kingdoms were active enough

- At the Age of Tranquility Kingdom could have one Hostile one time only.

- Next Age (Age of Turmoil) Peace can declare only for Hostile Kingdom

- At Age of War rules changes once more. Classical now, only less unfriendly Kingdom could declare War (if one of them is at Hostile, second - minimum Unfriendly) and no need to declare Hostile

- This 29th Age Peace was upgrade to Ceasefire. Also Unfriendly appeared.

- Next Age (Age of Unity) Stances appeared. Normal, Peaceful, Fortified and Aggressive

- At the Age of Conspiracy removed Peaceful Stance was removal

- It looks like conditions of End War never changes

**Politics**:

- Politics  looks like now mostly in all Ages: need to have  more than 50% of Kingdom Networth or been elected by maximum votes, not less then 35%

- First Kingdom Heads were prudish, so they call them-self Regents

- At Sixth Age Heads begin call them-self King or Queen (Monarch in common case).

- At Age of Conflict, minimum % to be elected changes to 60%

- Since next Age (Age of Nobility) minimum % was changed to 50%, and have lead minimum 2 votes from anybody else.

**Dragons**:

- We have too low information in was almost unwritten anywhere

- At least since 3rd Age Dragons exist. The Head of Kingdom  start the Project against Kingdom. There were no species, just one Dragon and only solders could kill him.

- At the Age of the Dragon system changed: there are several species of Dragon: Ruby Dragon, Emerald Dragon, Sapphire Dragon and Gold Dragon. And both specialists and solders could kill him

**Age's Names**:

- At World of Legend was 4 unique named Ages: as Generation, Revolution, Awakening and Call to Arms

- 5 Ages was named as an Era

- Rest of ages were named as Age

## Aggressive Actions

### Aggressive Actions

When abandoning a province, deserting, defecting and/or other province reset will be blocked by the following "aggressive actions".

#### Not Aggressive

- Cast Ritual

- Cast Self Spell

- Training

- Allocating Books

- Moving Scientists

- Receive Aid

- Building Acres

- Exploring

- Dragon fund

#### Aggressive

- Send Aid

- Use of any Espionage Op

- Use of any Sabotage Op

- Any army attack (tm/mass/plun/conq)

- Use of any Offensive Spell

- Dragon slay

## Aid

As you grow in Utopia, you will find that your Kingdom is like family. You share a special bond with them that makes their success just as important to you as your own might be. Provinces are welcome and encouraged to assist either other in times of need. Provinces can also use the Aid System to create their own barter commerce - trading food for runes or gold, and so on.
However, there are some taxes associated with Trade. Unfortunately, this is simply a reality of the Utopian World -- the Lords use these taxes to supply some of the services they offer and enforce the regulations they set. Your province maintains a Trade Balance that records the history of aid you have sent and received. Each time you send an Aid Shipment to a fellow province in your Kingdom, you will be given a Trade Surplus as described below, and the recipient will receive a Trade Deficit. Each day, a small portion of your trade balance will naturally be forgiven. You can find your current Tax Rate on shipments being received within your Aid Page.
Starting Age 68, sending Aid counts as an aggressive action. Certain actions (such as accepting an invitation) requires at least 24 hours since the last aggressive action.

### Contents

- 1 Aid: The Trade Balance

- 2 Aid: The Trade Tax

- 3 Aid & Tax Formulas

3.1 Max Shipment
3.2 Tax

#### Aid: The Trade Balance

Your province maintains a Trade Balance that records the history of aid you have sent and received. Each time you send an Aid Shipment to a fellow province in your Kingdom, you will be given a Trade Surplus, and the recipient will receive a Trade Deficit. Your Trade Balance is determined on this basis:
Resource Trade Value

- Gold: 1gc

- Food: 0.05gc

- Soldiers: 100gc

- Runes: 3gc

- Land: 1500gc (pulled from Explore Pool, but 1/3 will be destroyed)

Each Utopian Month, 10% of your Trade Balance will naturally decay, so that aid will be forgotten over time. This does not happen during War.

#### Aid: The Trade Tax

Trade recipients are taxed based on their accumulated Trade Deficit - Trade Surpluses are not taxed. The Tax Rate is based on the Province's relative Net Worth and Trade Balance, and will simply confiscate a portion of the traded goods. Tax takes effect once your negative Trade Balance reaches 400% of your Net Worth. If the Province is below the average Net Worth of the Kingdom, then the Tax Rate is calculated using the average instead.
Aid to needy Provinces is sometimes exempt from taxation. This aid still accumulates in the Trade Balance of both parties.

### Aid & Tax Formulas

#### Max Shipment

**Max Aid Shipment =** Province Net Worth * 4

#### Tax

**Base Tax Rate =** -4 * (Trade Balance / MAX (Net Worth, KD Average Net Worth) + 4)

**Tax Rate =** *DEPEND* ( Base Tax Rate ) :
                    Base Tax Rate < 0    = 0
               0 <  Base Tax Rate < 80   = Base Tax Rate
                    Base Tax Rate > 80   = 80

- Tax Rate is capped at 80% max.

- If the province is below the Kingdom's average Net Worth, its Tax Rate is calculated on the average Kingdom province Net Worth.

- If the province is below 25% of the Kingdom's median Acres, its Tax Rate is capped at 15%.

- Taxes don't take effect until your negative trade balance reaches 400% of your net worth (equivalent to one maximum aid shipment).

## Alliances

CONTENTS: Alliances | CONTENTS: Alliances
--- | ---
CONTENTS: Alliances

This is a contents page for the category **Alliances**. When you are creating a new Article/Page for an Alliance, use the following code:
{{Alliance}}
{{Infobox_Alliance
|name=
|tag=
|founder=
|leaders=
|website=
|contact=
|kingdoms=
}}

### Contents

- 1 Utopian Society

- 2 What are Alliances?

- 3 Purpose of Alliances

- 4 Informal Relations within the Society

4.1 Mutual Assistance Pacts (MAPs)
4.2 Mutual Defensive Pact (MDPs)
4.3 Non Aggression Pact (NAPs)
4.4 Diplomatic Assistance Pact (DAPs)
4.5 Non Alliance War Pact (NAWPs)
4.6 Friendly

- 5 World of Legends Alliances

5.1 Active
5.2 Disbanded

- 6 Genesis Alliances

6.1 Active
6.2 Disbanded

### Utopian Society

Players are encouraged to interact with other players in the same kingdom; each kingdom has a private forum that is accessible only to its members. Players that do not wish to remain in the kingdom they are assigned to can defect to another kingdom. However, defecting costs 15% of everything a player owns -- land, military, honor and resources -- and is generally used as a last resort. Players are limited to three defections for each Utopian age, and unused defections are lost at the end of the age.

### What are Alliances?

Alliances are a group of kingdoms which have chosen to band together and operate as a group.
They are not officially endorsed by the game creator or maintainers, and may be disdained by other players, however they are tolerated as a "necessary evil".

### Purpose of Alliances

The first organized alliances rose as defense against "unofficial" alliances (not public, just friends working together etc) or multies. Some of those Alliances were formed as a result of the game makers decision to breakup the Kingdoms in the early ages (affectionately known by some players as the Great Kingdom Split around age 3 or 4) designed to allow people the chance to play with and get to know other players in the game.
Through the ages however alliances have also formed for a variety of other reasons from almost purely social, often nationality-based ones, via educational ones, to defensive ones whose main purpose is to defend their members against "unfair play", and finally to offensive ones who actively use their alliance to gain advantages over others. They often employ tactics that single kingdoms can not use, such as overwhelming an opponent by outnumbering them. The mechanism for the game eventually changed and current ages are allowed to invite friends to join them in their Kingdoms.

### Informal Relations within the Society

#### Mutual Assistance Pacts (MAPs)

Each MAP has it's own unique set of terms that are confidential between the two alliances, but in general, an alliance means that in an alliance war, we will assist, or be assisted by these alliances if needed. No aggressive actions of any kind are permitted between allied kingdoms.

#### Mutual Defensive Pact (MDPs)

Each MDP has it's own unique set of terms that are confidential between the two alliances, but in general, the pact means that in an alliance war, we will assist, or be assisted by these alliances if needed. Allows friendly exchanges and hostilities to exist between individual members and kingdoms, as long as an honorable code of conduct exists between both parties. Kingdom wars are allowed, only alliance wars are off limits.

#### Non Aggression Pact (NAPs)

A non-aggression pact is a weaker relationship than an alliance. No aggressive actions of any kind are permitted between NAP'd kingdoms, but no formal obligation to assist in an alliance war exists.

#### Diplomatic Assistance Pact (DAPs)

DAP status indicates a commitment on the part of the 2 alliances to provide diplomatic assistance to each other in time of need. Random attacks and 1:1 wars are permitted between members of the alliance.

#### Non Alliance War Pact (NAWPs)

An alliance war will never exist between the two alliances. Allows friendly exchanges and hostilities to exist between individual members and kingdoms, as long as an honorable code of conduct exists between both parties. Kingdom wars are allowed, only alliance wars are off limits.

#### Friendly

Friendly status indicates a commitment on the part of the 2 alliances to work towards closer relations, and a preference to avoid conflict at the alliance level. At friendly level, random grabs and 1 vs. 1 kingdom wars of a duration lasting between 48 hours and a maximum of 54 hours are permitted. 12 hour hostiles with a max time of 24 hours are also allowed, as is limited duration random thievery and magic operations.

### World of Legends Alliances

#### Active

- Absalom

- Apocalypse Alliance

- Honor & Justice

- Hybris

- Kaer Loche Alliance

- Lotus

- Nex Imperio

- Knights Templar

- Order of Avalon

- Nation of Hope

- Semper Fidelis

- Taure en'Arvandor

- Truidian Federation

#### Disbanded

- Global Swords Alliance

- Crazy Slaughtering Brotherhood

- Death in Existence

- The Brotherhood

- 9 Fates

- United Angels

- Visions of Fianna

- Covenant

- NeXt Community

- Art of Destruction

- Brotherhood of the Dragon

- Asian Triads

- Echo

- Eternal n Deadly

- EXodus

- Integrity Alliance

- IHJ

- mperial Alliance

- NewLife

- Republic of Utopia

- Solace

- Shire of Secrecy

- The Black Horde

- The Dreaded Community

- Tabula Rosa

- United Council

- UGL

- The Dark Knights

- Ninjas in Pajamas

- Warriors Attack and Retaliation

- Wolves of Death

- Nordic Alliance

- Divine Titans

### Genesis Alliances

#### Active

- No one (This server is inactive)

#### Disbanded

- RAH

- Destructive Aftermath

- Showdown

- V Alliance

- Imperial Order

- Snugz4Funky

- PSY Alliance

- DP Alliance

- Brotherhood of Ancient Kings

- Cataclysmic Retribution

### Pages in category "Alliances"

The following 21 pages are in this category, out of 21 total.

#### A

- Template:Alliance

- Template:Alliance Disbanded

- Alliance:Absalom

- Alliance:Apocalypse Alliance

- Alliance:Crazy Slaughtering Brotherhood

- Alliance:Death in Existence

- Alliance:Global Swords Alliance

- Alliance:HaJ

- Alliance:HaLL

- Alliance:Hybris

- Alliance:Kaer Loche Alliance

- Alliance:Knights Templar

- Alliance:Lotus

- Alliance:Nation of Hope

- Alliance:Nex Imperio

- Alliance:Order of Avalon

- Alliance:Semper Fidelis

- Alliance:Sisterhood of Utopia

- Alliance:Taure en'Arvandor

- Alliance:Truidian Federation

- Alliance:Zen

## Ambush Guide

This is part of the Utopia WIKI Mini Guide Series.
---

THIS PAGE describes a game mechanism - Guide:Ambush in utopia. It also aims to discuss the implications of this game mechanism & how others have utilized it. To discuss further implications or ask questions with regards to Guide:Ambush, be sure to check out the discussions page. | THIS PAGE describes a game mechanism - Guide:Ambush in utopia. It also aims to discuss the implications of this game mechanism & how others have utilized it. To discuss further implications or ask questions with regards to Guide:Ambush, be sure to check out the discussions page.
--- | ---
THIS PAGE describes a game mechanism - Guide:Ambush in utopia. It also aims to discuss the implications of this game mechanism & how others have utilized it. To discuss further implications or ask questions with regards to Guide:Ambush, be sure to check out the discussions page.

### Contents

- 1 Why Ambush?

- 2 Notes About Ambush

- 3 How to figure out how much offense to send

3.1 Example

- 4 Addition Information

### Why Ambush?

- To kill troops (especially if your target is an Orc with Elites in the army).
 Why? --> They have an insanely low defensive value elite.
 Why? --> Ambushes are 25% faster than normal attacks.

- To decrease your target's incoming land (especially if your target is a chain target).

- Because you're able to Ambush + Trad him and want to rub it in his face.

### Notes About Ambush

- You can ambush each successful attack once. If you fail, too bad.

- You cannot ambush if your opponent used Anonymity or War Spoils.

- You cannot ambush a hit from a personality or race that has full ambush protection.

- If you successfully carry out an ambush you will recapture 50% of his captured land (unless the target has an ambush protection or vulnerability modifier)

- You ALWAYS ambush the most recent hit of the province you select UNLESS Anonymity or War Spoils were used.
 You will ambush the last successful hit that did not use Anonymity or War Spoils.
 You CAN ambush an ambush.

### How to figure out how much offense to send

- Take an SoM

- Record the value of troops out in the SoM.

- Once you have obtained these numbers, use this formula:

**Raw Offense Required =** [(Target's Elites sent * Racial Elite Defense Value) + (Target's Off Specs Sent * Racial Def Spec Value) + (Target's Soldiers sent * (IF (Racial Soldier Defense Value = 0 , Racial Soldier Offense Value , Racial Soldier Defense Value))] * 0.8

**Note:** If racial Soldier Defense Value is 0, the Offense value will be used instead
*Remember, this is the **RAW** Offense required - therefore, don't bother sending more than 1 general, they have no effect!*

#### Example

*June 4th, YR5 call (XX:XX) invaded Kzagl (XX:XX) and captured 81 acres of land.
June 4th, YR5 I just been (XX:XX) invaded Kzagl (XX:XX) and captured 139 acres of land.
June 4th, YR5 piercing through (XX:XX) invaded Kzagl (XX:XX) and captured 131 acres of land.*
**Kzagl** didn't take particularly kindly to these attacks, and thought it would be a good idea to ambush one of them, so he took a SoM of **I just been**, the largest hit against him, to see what troops had been sent out against him and whether it was a good idea to ambush.
**SoM on I just been**
*** Army #2 (Back in 10:46 hours) ***
*
*Ogres: 4,424 (58,397 offense / 9,733 defense)
*Captured Land: 139 Acres*
On seeing the no specialists (goblins) and high amount of elites (ogres), Kzagl made the decision to get a few of his acres back
So, basically the target sent 4424 ogres (well, he sent a few more, but lost some in the attack) to attack **Kzagl**. If he had sent some soldiers or specialists (or both) you'd see them also in the SoM. Now we can calculate what is going to be required to successfully ambush.
Orc elites are great for attacking with, not so great for defending with. Because they only have 2 defense (note values change form age to age, this is an example only), that's what they defend with on an ambush.

Therefore, 4424 Elites * 2 Defense Value = 8,848

The defense will fight at 80% of its normal capacity.' So, we multiply that number by 0.8

8,848 * 0.8 = 7078.4

Now, this is another important bit, when we calculate how much offense we're going to send, we don't modify it in anyway. If you're using angel's military calculator to do it, make sure you use the **RAW OFFENSE** number.
If you are just sending (6/0) offensive specialists at the target, you would require:

7079/6 = 1,770 off specs (rounded up)

- Sending more than one general does not increase your offense.

- Training Grounds, Military wages, Aggression, and Fanaticism do not affect ambush offense.

If you set your attack to Ambush on the war room then the game will accurately display the offence you are about to send.
You always ambush the last hit made against your province by your target as long as the armies are still marching home with captured land.
So if the paper had looked like this:
*June 4th, YR5 I just been (XX:XX1) invaded Kzagl Elven Grave (XX:XX) and captured 139 acres of land.
June 4th, YR5 piercing through (XX:XX) invaded Kzagl Elven Grave (XX:XX) and captured 131 acres of land.
June 4th, YR5 I just been (XX:XX) invaded Kagl Elven Grave (XX:XX) and captured 25 acres of land.*
You would have to ambush the hit for 25 acres before you could ambush the hit for 139 acres. You wouldn't necessarily have to be successful though and could send 1 soldier and 1 general, because once you've ambushed a hit by a province, you can't ambush that hit again, so the game moves onto the next hit.

### Addition Information

- Ambush

- War Room

## Ambushing

Conflict is at the heart and soul of the fine world of Utopia. While peace has it's place, combat is what makes the world go 'round here. Conquering others is your way of making a name for yourself around the world. But beware -- too many enemies and you may not live to see tomorrow. I cannot make you a masterful leader - that can only be learned through experiences of success and patience through failures, but I will share what I can.

### Contents

- 1 Military Units

1.1 Understanding Attacks
1.2 Attack Times
1.3 Random Factor

- 2 Other Factors:

2.1 War Horses
2.2 Mercenaries
2.3 Prisoners
2.4 Specialist Credits
2.5 Building Credits

- 3 Your Attack Options

3.1 Traditional March
3.2 Raze
3.3 Plunder
3.4 Learn
3.5 Massacre
3.6 Conquest
3.7 Ambush

- 4 Addition Information

### Military Units

To attack other provinces you must deploy armies comprised of different kinds of military units (Horses, Prisoners, Mercenaries	, Solders, Offensive Specialists, Defensive Specialists, Elites, Generals). You must have sufficient units of each type drafted and/or trained. See Units for more information.
You can view each races unit strengths through the games Race & Personality details page.

#### Understanding Attacks

With risk comes reward. Remember this forever during your time here in Utopia. There will be plenty of opportunities to attack the smaller, weaker lands around the world. There will be plenty of bullies looking to attack you. There will be plenty of chances to feed on the remains of provinces ravished by others. The Lords understand this is not noble, and they will see to it that this behavior is not rewarded.
**You will quickly find that attacking others of similar networth to yourself will be richly rewarded.** Attack smaller enemies and you will suffer a variety of penalties - gaining less and finding your army away for long periods. You will also find that attacking within your own kingdom has few, if any, rewards.

#### Attack Times

Attacks are missions which take both time and effort to carry out, and subsequent rest for your military forces. Attacks will require about 14 days (baseline) to complete -- this includes time spent attacking, resting, and preparing your new land or other resources for use. A variety of factors can affect this base time, including the size of your opponents. Attacking vastly different size opponents will result in higher attack times. You will find this information shown on the Attack Menu within your War Room.

#### Random Factor

As of age 103, the random factor has been removed. Attacks will now always succeed when Mod Offense sent is equal to at least Mod Defense +1.

### Other Factors:

#### War Horses

War Horses are produced from stables and allow your military to fight with more power. You may include up to one horse per military unit sent in combat, and each offers 2 additional point of offensive strength.

#### Mercenaries

In addition to your own troops, you will may also hire mercenaries to help in attacks. These mercenaries are paid to serve under you for only a single attack. For a hefty price, these can increase your attack capabilities substantially, 8 points per mercenary. You will also learn that you can capture and hold enemy prisoners of war to serve as free mercenaries through the construction of Dungeons on your lands.

#### Prisoners

Prisoners are taken from the total number of enemies that would've been killed after an attack, usually at a 2/3 prisoner to total kills ratio - IF there is room in your dungeons for them.
Prisoners have no upkeep, every 2 prisoners fill 1 job (only for BE calculations), and every prisoner produces 0.75gc per hour (regardless of whether or not there are unfilled jobs). For the formula, please refer to Economy.
About one third of the prisoners sent are lost in the fight. They are then again immediately available to your general. Each prisoner sent in your attack will provide 8 offensive points.

#### Specialist Credits

On successful Traditional March attacks you earn credits allowing for specialist units to be trained at no gc cost. The amount of credits gained is directly related to the amount of defense you break. Defense *.008 * Relative Networth is the base formula.
These will decay while out of war at a rate of 20% at the dawn of each Utopian Month. Upon leaving End-of-War Ceasefire, all credits will be lost. You also have the option to not use credits when training units.

#### Building Credits

On successful Traditional March attacks you earn credits allowing for buildings to be built or razed with no gc cost. The amount of credits is tied to nw but the exact formula is currently unknown. It is estimated to have a base of approximately: acres taken * 0.4 * rel nw.
These will decay at a rate of 20% at the dawn of each Utopian Month **IF** your total credits are greater than 15% of your total land (Credits > Acres * 0.15). Upon leaving End-of-War Ceasefire, all credits will be lost. You also have the option of not using credits when building.

### Your Attack Options

#### Traditional March

The standard attack - captures a portion of enemy lands.

#### Raze

Simply destroys a portion of the enemy lands and is not affected by differing province sizes.
Only destroys buildings during War.

#### Plunder

Captures some of an enemy's gold, food, and runes. Troop losses on Plunder defense are reduced by 50%.

#### Learn

Steals a portion of target's allocated Books plus a portion of the target's unallocated Books.
During War, Learn temporarily removes part of target's Science Books.
Troop losses on Learn defense are reduced by 50%.

#### Massacre

Rampages through a province killing any population that can be found, including peasants, wizards, and thieves. Damage increased during War.

#### Conquest

Similar to a Traditional March, but does not need to be fully successful to capture land. It is limited to opponents of very similar in size to yourself, except in War.

#### Ambush

Can be conducted against a province that has recently captured land from you. Strike an opponent's army away from home and recaptures 50% of the land stolen from you. Because of its surprise nature, no offensive or defensive modifiers are considered - only raw military strength - and the defense will fight at 80% of its normal capacity. Specialists in the opposing army will defend with the strength of defensive specialists of that race. A province attacking Anonymously or using War Spoils cannot be ambushed. An army can only be ambushed once. Ambush inflicts increased Military Casualties.
Be sure to check out the Ambush Guide if you are still unclear.

### Addition Information

- Attacking & Defending

- Units

## Assassinate wizards

No one ever said leadership involves only public activities. With a state-sanctioned paramilitary thieves guild available to you, the possibilities are endless. What may not be possible through war or magic may still be possible with deceit and deception. Never underestimate the power of the underground unknown.
Thieves are professional soldiers, trained in the arts of the elite underground and are trained on your Military Menu. They maintain a Stealth Rating which determines when they can be used. This rating rises automatically each day by 3 points and drops each time your thieves conduct an operation. Your thieves will not carry out missions without at least a 5% Stealth Rating.
The best measure of your guild's strength is the number of thieves you maintain per acre of land, often known as Thieves Per Acre (TPA), modified by your Thieves' Dens, your Crime science and your racial bonuses or penalties. The success rate of your guild depends on both your and your target's TPA. The raw damage, however, is based on raw strength - the more thieves you use in an operation, the more damage they can do.
The larger your province, the more difficult it will be to keep your guild well-organized and efficient. As your province grows larger, be prepared to keep training additional thieves to keep your network intact and effective. Like most things in Utopia, thievery operations are easier and more effective against provinces similar to you in size.
Information on how to calculate thief operations can be found here.
Thievery operations are divided in two categories, as listed below:

- Espionage Operations

- Sabotage Operations

### Contents

- 1 The Thieves' Toolbox: The Espionage Operations

1.1 Spy on Throne
1.2 Spy on Defense
1.3 Spy on Exploration
1.4 Snatch News
1.5 Infiltrate
1.6 Survey
1.7 Spy on Military
1.8 Spy on Sciences

- 2 The Thieves' Toolbox: The Sabotage Operations

2.1 Sabotage Wizards
2.2 Destabilize Guilds
2.3 Rob the Granaries
2.4 Rob the Vaults
2.5 Rob the Towers
2.6 Kidnapping
2.7 Arson
2.8 Greater Arson
2.9 Night Strike
2.10 Incite Riots
2.11 Steal War Horses
2.12 Bribe Thieves
2.13 Bribe Generals
2.14 Free Prisoners
2.15 Assassinate Wizards
2.16 Propaganda

- 3 Changelog

### The Thieves' Toolbox: The Espionage Operations

The espionage operations will simply gather information regarding the enemy province.
Nevertheless, sending **5% of your thieves will return completely accurate results** .

#### Spy on Throne

 Available to:       All
 Relations Required: All
 Effect:             Gives an estimate of the resources and troops available to a province
 Difficulty:         very low
 Meter Movemement:   0

- Consumes only 1% Stealth

#### Spy on Defense

Reports enemy's standing defenses.

 Available to:       All
 Relations Required: All
 Effect:             Reveals Net Defensive Points at Home
 Difficulty:         very low
 Meter Movemement:   0

- Consumes only 1% Stealth

#### Spy on Exploration

Gives current pool size, and costs per acre in gold and soldiers.

 Available to:       All
 Relations Required: All
 Effect:             Reveals pool size, and costs per acre in gold and soldiers.
 Difficulty:         very low
 Meter Movemement:   0

#### Snatch News

 Available to:       All
 Relations Required: All
 Effect:             Displays the targeted provinces Kingdom Paper
 Difficulty:         low
 Meter Movement:     0

#### Infiltrate

Reports on the size of your opponent's guild.

 Available to:       All
 Relations Required: All
 Effect:             Gives an estimate of the number of thieves in the enemy province.
 Operation Message:  Our thieves have infiltrated the Thieves' Guilds of [province name] (##:##). They appear to have about X thieves employed across their lands.
 Difficulty:         low
 Meter Movement:     0

#### Survey

Reports on the distribution of buildings in a province.

 Available to:       All
 Relations Required: All
 Effect:             Gives an estimate of the buildings in the enemy province, as displayed by the Internal Affairs advisor.
 Operation Message:
 Difficulty:         low
 Meter Movemement:   0

#### Spy on Military

Provides detailed information from your opponent's army.

 Available to:       All
 Relations Required: All
 Effect:             Shows the enemy troops out as well as an estimate of troops at home and in training,
                     as displayed by the Military Advisor.
 Operation Message:
 Difficulty:         low
 Meter Movemement:   0

#### Spy on Sciences

Estimates strengths and effects of opponent's science levels.

 Available to:       All
 Relations Required: All
 Effect:             Gives an estimate of the bonuses an enemy province gains from its science, as displayed on the Science page.
 Operation Message:
 Difficulty:         low
 Meter Movement:     0

### The Thieves' Toolbox: The Sabotage Operations

Listed here is a short reference guide to each of the offensive operations available to you and their effects. As mentioned previously, sending more thieves will increase the strength of these operations. Nevertheless, sending too many thieves also increases the chances that the enemy catches your men! Certain operations are designated Unfriendly, Hostile or War Only operations -- Because of the destructive nature of these operations, they can be run only against provinces which have at least a certain level of relations with your kingdom. In addition, you will find that many operations are more effective during heightened relations conditions.

#### Sabotage Wizards

Drains the target's Mana levels for several days, limiting the ability to cast spells.

 Available to:       All
 Relations Required: Unfriendly
 Effect:             Reduces Mana level by 5% of current level each Tick, before Mana regeneration.
 Operation Message:  Our thieves have sabotaged their wizards' ability to cast spells.
 Difficulty:         medium
 Meter Movement:     0

#### Destabilize Guilds

Decreases the target’s Spell Duration for several days.

 Available to:       Rogues
 Relations Required: All
 Effect:             Decreases the target’s Duration of Self Spell and Offensive Spell casts while the effect is active by 20%.
 Operation Message:
 Difficulty:         medium
 Meter Movement:     0

#### Rob the Granaries

Steals food from your opponent's storages.

 Available to:       All
 Relations Required: All
 Effect:             Steals up to a max of 31.5% (46% in war) enemy food at the rate of 95 (135 in war) bushels per thief.
 Operation Message:  Our thieves have returned with X bushels.
 Difficulty:         medium
 Meter Movemement:   0.06

#### Rob the Vaults

Steals gold from enemy coffers.

 Available to:       All
 Relations Required: All
 Effect:             Steals up to a max of 5.2% (14% in war) enemy gc at the rate of 40 (106 in war) gc per thief.
 Operation Message:  Our thieves have returned with X gold coins.
 Difficulty:         medium
 Meter Movement:     0.12

#### Rob the Towers

Steals runes from your target's wizards.

 Available to:       All
 Relations Required: All
 Effect:             Steals up to a max of 24.5% (35% in war) enemy runes at the rate of 18.2 (26 in war) runes per thief.
 Operation Message:  Our thieves were able to steal X runes.
 Difficulty:         medium
 Meter Movement:     0.09

#### Kidnapping

Kidnaps peasants from your enemy and brings them to your province.

 Available to:       All
 Relations Required: All
 Effect:             Steals up to a max of 1.85% (4% in war) enemy peasants at the rate of 0.132 (0.285 in war) peasants per thief.
 Operation Message:  Our thieves kidnapped many people, but only were able to return with X of them.
 Difficulty:         medium
 Meter Movement:     0.12

You can also refer to Thievery Formulas for more information. Note that gains seem to drop by 50% when the enemy province reaches a certain level of under population. This is designed to make it harder to player-kill.

#### Arson

Burns down enemy buildings to disrupt an enemy's stability.

 Available to:       All
 Relations Required: All
 Effect:             Destroys a small amount of enemy buildings.
 Operation Message:  Our thieves burned down X acres of buildings. OR  Unfortunately, our thieves were too few in number to find any buildings to burn.
 Difficulty:         medium
 Meter Movement:     0.24

#### Greater Arson

A more powerful version of Arson, this operation allows targetting of a specific type of building to burn down. Only Rogues can master this difficult operation.

 Available to:       Rogues
 Relations Required: Unfriendly
 Effect:             Destroys up to a max of ~6% of targeted enemy buildings at the rate of 0.0045 buildings per thief.
 Operation Message:  Our thieves burned down X [building type].
 Difficulty:         Medium
 Meter Movement:     0.3

#### Night Strike

Assassinates a portion of your enemy's military, both at home and away.

 Available to:       All
 Relations Required: Unfriendly
 Effect:             Kills up to a maximum of 16.25% enemy soldiers at a rate of 0.67 soldiers per thief.
                     Also kills a much smaller amount of specialists and elites. Will affect all troops, even those that aren't home.
 Operation Message:  Our thieves assassinated X enemy troops.
 Difficulty:         medium
 Meter Movement:     0.24

#### Incite Riots

Incites riots which disrupt tax collection efforts for several days.

- The More thieves you send the higher your min, avg, max duration will be

- Unaffected by Sabotage damage bonus

 Available to:       All
 Relations Required: All
 Effect:             Decreases targets income by 15%.
 Operation Message:  Our thieves have caused rioting. It is expected to last X days.
 Difficulty:         medium
 Meter Movement:     0.18

#### Steal War Horses

Steals an enemy's horses for your own use.

 Available to:       Rogue
 Relations Required: Unfriendly
 Effect:             Steals up to 20% of the targets horses at a rate of 0.35 horses per thief.
                     Note that you only gain half of this number as the rest are released.
 Operation Message:  Our thieves were able to release X horses but could only bring back Y of them.
 Difficulty:         medium
 Meter Movement:     0.18

#### Bribe Thieves

Reduces the ability of an enemy thieves' guild to conduct and defend against thievery operations until the double agents are caught by the enemy.

 Available to:       All
 Relations Required: All
 Effect:             Reduces thief effectiveness by 10%
 Operation Message:  Our thieves have bribed members of our enemies' guild!
 Difficulty:         medium
 Meter Movement:     0.09

#### Bribe Generals

Increases the losses sustained by your enemy in all combat until the bribed generals are discovered by the opponent.

 Available to:       All
 Relations Required: All
 Effect:             Effectively a 1 in 5 chance per attack to increase troop losses by 20% on all combat.
 Operation Message:  Our thieves have bribed an enemy general!
 Difficulty:         medium
 Meter Movement:     0.09

#### Free Prisoners

Releases prisoners from an opponent's dungeons. You gain half of them.

 Available to:       All
 Relations Required: All
 Effect:             Releases up to a max of 12% (17% in war) of the targets prisoners at a rate of 0.06 (0.07 in war) prisoners per thief.
 Operation Message:  Our thieves freed X prisoners from enemy dungeons.
 Difficulty:         medium
 Meter Movement:     0.03

#### Assassinate Wizards

Attempts to assassinate enemy wizards to permanently weaken their ability to cast spells. Only Rogues can master this difficult operation.

 Available to:       Rogues
 Relations Required: Unfriendly
 Effect:             Kills up to a max of 1.2% target wizards at a rate of 0.006 wizards per thief.
 Operation Message:  Our thieves assassinated X wizards of the enemy's guilds!
 Difficulty:         high
 Meter Movement:     0.36

#### Propaganda

Attempts to convince enemy peasants, military, or wizards to revolt and join your province. Only Rogues can master this difficult operation.

 Available to:       Rogues
 Relations Required: War
 Effect:             not fully determined
 Operation Message:  We have converted X [wizards, thieves, soldiers] from the enemy to our guild.
                     OR  We have converted X [of the enemy's specialist troops, (elite unit name) from the enemy] to our army.
 Difficulty:         high
 Meter Movement:     0 (War Only)

### Changelog

- Age 106: Meter movements updated to reflect forum changes of "all values have tripled" on 6 May 2024.

- Age 106: NS updated to reflect 25% more damage on 29 May 2024.

## Attacking & Calculating an Attack

This is part of the Utopia WIKI Player written guides.
---

THIS PAGE is a guide aimed to cover Attacking & Calculating an Attack. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page. | THIS PAGE is a guide aimed to cover Attacking & Calculating an Attack. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.
--- | ---
THIS PAGE is a guide aimed to cover Attacking & Calculating an Attack. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.

### Before Attacking

- Check that your target isn't in a war.

- Retrieve your target's defense.

- Check if you casted relevant self-spells (War spoils, Quick feet, Fanaticism, Anonymity etc.).

- Check that you are sending the right amount and type of troops generals.

- Check that you're sending the right number of generals, do NOT send 4 when you need to make more than one hit.

- Check the attack type (if you click back when hitting the second time, remember to set it again).

- Check if the target is online (he could have casted protective self-spells in order to make you bounce).

- Make sure the hour hasn't ticked since you got your intel.

- Recheck Intel.

- Hit the button.

### Retrieving your Target's Defense

- Get a Spy on Military

### Calculating An Attack

**Modified Offense you need to send =** (Target Def + 1)

- Intel gathered using 5% of your thieves will be accurate.

## Buildings

Your growth page lets you build up your acres with a variety of buildings.  The Build Table below can help provide details on the benefits of the different buildings for your Province.
In Utopia, your **Growth** page provides information on:

- Total Land

- Total Undeveloped Land

- Construction Time

- Free Building Credits

- Construction Costs

- Maximum Buildable Now

- Raze Cost

- Maximum Razeable Now

Additionally, the **Growth** page will show you a list of all possible buildings along with the following information for each building:

- The amount of each building you own

- The amount of each building in progress

To build a building, just input the amount desired of the building you wish to build in the construct space next to the building you wish to build, then click construct buildings.
The **Growth** page also gives you the option to:

- accelerate the construction of your building

- whether or not to use available credits

- and the option to either raze or cancel buildings.

### Contents

- 1 Build Table

- 2 Classes of Buildings

- 3 The Buildings

3.1 Barren Land
3.2 Homes
3.3 Farms
3.4 Mills
3.5 Banks
3.6 Training Grounds
3.7 Armouries
3.8 Military Barracks
3.9 Forts
3.10 Castles
3.11 Hospitals
3.12 Guilds
3.13 Towers
3.14 Thieves Dens
3.15 Watch Towers
3.16 Universities
3.17 Libraries
3.18 Stables
3.19 Dungeons

- 4 Retired buildings

- 5 Construction

5.1 Construction Time
5.2 Construction Costs
5.3 Raze Costs

- 6 Buildings

6.1 Building Efficiency
6.2 Building Effects

- 7 Changelog

### Build Table

Note: Capacity of buildings is not affected by Building Efficiency (i.e., Homes, Stables, Dungeons can hold the specified number regardless of BE).

Building | Capacity | Flat Rate Base | Percent Base Effect | Percent Effect Max | Living Space | Jobs | Description
--- | --- | --- | --- | --- | --- | --- | ---
Barren Land | 15 People | 2 Bushels |  |  | 15 | 0 | Houses 15 people and Produces 2 bushels per hour (Unaffected by BE)
Homes | 10 People | 0.3 Peasants† |  |  | 35 | 0 | Houses 10 additional peopleGenerates Peasants per day (Unaffected by BE)
Farms |  | 60 Bushels |  |  | 25 | 25 | Produces 60 bushels per day
Mills |  |  | 4%3%2% | 100%75%50% | 25 | 25 | Decreases Build Costs Decreases Gold Exploration CostsDecreases Soldier Exploration Costs
Banks |  | 25gc | 1.5% | 37.5% | 25 | 25 | Produces 25gc per dayIncrease in Income
Training Grounds |  |  | 1.5%1% | 37.5%25% | 25 | 25 | Increases Offensive Military EfficiencyReduces Training Time
Armouries |  |  | 2%2%1.5% | 50%50%37.5% | 25 | 25 | Decreases Draft CostsReduction of WagesDecreases Training Costs
Military Barracks |  |  | 1.5%2% | 37.5%50% | 25 | 25 | Lowers Attack TimeReduced Mercenary Costs
Forts |  |  | 1.5% | 37.5% | 25 | 25 | Increases Defensive Military Efficiency
Castles |  |  | 2.25%2% | 50%50% | 25 | 25 | Decreases Resource (Land, Gold, Food, Runes, Books) Losses when AttackedDecreases Honor Losses when Attacked
Hospitals |  |  | 3%3%2% | 75%75%50% | 25 | 25 | Decreases Military LossesDaily Chance of Curing the PlagueIncreased Birth Rate
Guilds |  | 0.02 Wizards† |  |  | 25 | 25 | Wizards Trained per day (Unaffected by BE)Guilds also increase Spell duration (Unaffected by BE)
Towers |  | 12 Runes |  |  | 25 | 25 | Produces 12 runes per day
Thieves Dens |  |  | 3.6%3% | 90%75% | 25 | 25 | Lowers losses in Thievery OperationsBonus to TPA
Watch Towers |  |  | 2.0%2.5% | 50.0%62.5% | 25 | 25 | Chance of Catching Enemy ThievesReduced damage caused by Enemy Thieves
Universities |  |  | 1.5%1% | 37.5%25% | 25 | 25 | Increase Scientist spawn rate (Unaffected by BE)Increases generation of Science Books (Unaffected by BE)
Libraries |  |  | 1% | 25% | 25 | 25 | Increase Science Efficiency (Unaffected by BE)
Stables | 80 Horses | 2 Horses |  |  | 25 | 25 | Houses War Horses and increases their production rate
Dungeons | 30 Prisoners |  |  |  | 25 | 25 | Houses Prisoners of War
Building | Capacity | Flat Rate Base | Percent Base Effect | Percent Effect Max | Living Space | Jobs | Description

† - this is a stacking chance per Tick, not Production

### Classes of Buildings

There are three classes of building effects, and each functions differently. While this may be difficult to follow, you will quickly understand it with some experience within the game. The three classes are:

 **Capacity Buildings** - These buildings simply create space for you, and are **not** impacted by efficiency
 issues. Homes, for example, provide additional space for peasants.

 **Flat Rate Buildings** - This type of building provides a set amount of a particular resource. These
 buildings need many employees to be fully effective. These buildings **are** impacted by building efficiency. An example is a Tower which creates a set
 number of runes each day.

 **Percentage-based Buildings** - The majority of Utopian buildings are percentage-based. These buildings
 provide an effect based on the portion of your land covered by it. For example, having 10% of your
 land as Banks will increase your income by a certain percentage. Like flat-rate buildings, these
 also require employees to provide full effects. In addition, each additional building you construct
 will be less effective. The numbers listed in this section would be for the first building you
 construct. Your Internal Affairs Advisor will help you to understand the benefits of your land.
 Unless otherwise specified, these buildings have a maximum effect of 25 times the number listed
 below. With normal building efficiency, this maximum is reached by dedicating 50% of your land to
 that building.

### The Buildings

#### Barren Land

Barren lands are not an actual building. These are simply available acres - gained by exploration, the Paradise spell or attacks - in your province that can be built up with real buildings as described below. Nevertheless, barren lands can still hold a few people and produce a very small amount of food every day.

- Increases your maximum population by 15 (built land has a base capacity of 25)

- Produces 2 Bushels per Day

#### Homes

While every built up acre of land already houses people – which means Homes are not a necessity for a province – you may find yourself wanting more population. Homes give your citizen more place to live, and also increase your natural birth rates. Furthermore, Homes employ no peasant and will thus overall help you fill all the jobs in your province.

- Increases your maximum Population by 10 (on top of the 25 that a completed Building provides, for a total of 35)

- Generates 0.3 extra Peasants per Tick (30% stacking chance to gain a Peasant per Home)
Affected by Chastity

- Employs no one

- Not affected by Building Efficiency

#### Farms

Farms are one of the most important buildings in your province, and also a vital one. Every day, each of your people will eat 0,25 bushels, and each Farm produces 60 bushels per day. Watch your food supplies very carefully, because otherwise starvation might deplete your population rather fast!

- Produces 60 Bushels Per Day

#### Mills

Exploration is one of the main ways of growing in Utopia, and building Mills will help you to send out expeditions at cheaper cost. Furthermore, Mills will also improve your builders skills, making building construction slightly less expensive.

- Decreases Building Costs by % * 4 (Max of 100%)

- Reduces exploration gold expenses by % * 3

- Reduces exploration soldier cost by % * 2

#### Banks

Banks are one of the major sources of income in Utopia along with tax collection. Every day, each Bank you own will produce some gold. Furthermore, your Banks all work together at improving your tax collection facilities, increasing further your global income.

- Generates 25gc per day

- Increases Income by % * 1.5

#### Training Grounds

Maintaining a good offense is important for all attackers, and Training Grounds bolster that by providing an enhanced training to all your offensive troops. This allows them to fight more efficiently in combat, thus increasing your overall attacking power.

- Increases Offensive Military Efficiency by % * 1.5

- Training Time reduced by % * 1

#### Armouries

Armouries improve your military training process, allowing you to train your soldiers to advanced levels at a cheaper cost. Armouries also facilitate your peasant enrolment process and diminish your military maintenance costs.

- Decreases Draft Costs by % * 2

- Decreases Daily Wages by % * 2

- Decreases Military Training Costs by % * 1.5

#### Military Barracks

Military Barracks are another military-oriented building. The employees of the Barracks are in charge of your military logistics, and a well-equipped army will reach the enemy land faster, making yourself less vulnerable to attacks while your troops are out on a campaign.

- Lowers Attack Time by % * 1.5

- Reduced Mercenary costs by % * 2

#### Forts

Forts provide a superior protection to the troops held in garrison in your province, increasing your overall defensive strength against attacks. Maintaining a good defense is important if you want to keep your acres and resources safe.

- Increases Defensive Military Efficiency by % * 1.5

#### Castles

Unlike Forts, Castles will not make you less vulnerable to attacks. Nevertheless, they will effectively protect your land, resources and honor, making the enemy’s attacks against your province less efficient.

- Decreases Resource (Land, Gold, Food, Runes, Books) Losses when Attacked by % * 2.25

- Decreases Honor Losses when Attacked by % * 1.5

#### Hospitals

Having a good military power is important, and keeping your soldiers healthy is vital in order to achieve this. By deploying Hospitals in the battlefields, you will significantly lower the casualties suffered by your troops in combat. Furthermore, your medics will work at curing the Plague if your province ever catches it.

- Decreases Military Casualties by % * 3

- % * 3 Daily Chance of Curing the Plague

- % * 2 Increased Birth Rate

#### Guilds

Unlike all your other units, either the military footmen or the thieves, wizards are not trained by using gold. Your ascendant wizards will have to go through intensive studies in Guilds before being able to serve you properly. They are an absolute necessity for Mages.

- Trains 0.02 Wizards per Tick (2% stacking chance to train a Wizard per Guild)

- Determines and Increases Spell Duration (capped at 20% Guilds)

- Increases Self Spell and Ritual success chance

Guilds also increase the duration of your Self and Offensive Spells.
Guilds are unaffected by BE (Building Efficiency) for the purposes of calculating Spell Duration or Wizards trained.

#### Towers

Towers are massive buildings that are used in order to channel mystic energies produced by the Earth into small stones called runes. Runes are then expended by your wizards while casting magic spells.

- Produces 12 Runes Per Day

#### Thieves Dens

Thieves Dens are the lair of all the thieves in your province, serving as the place where they practice their obscure and dark skills. Thieves Dens will increase the success rate of thievery operations you conduct as well as lowering your thief losses. Thieves Dens are a must for all Thieves.

- Lowers Losses in Thievery Operations by % * 3.6 (capped at 90%)

- Increases Thievery Effectiveness by % * 3

#### Watch Towers

While your own thieves can protect your land against enemy thieves, a little extra protection is never a bad thing. People assigned into Watch Towers will screen your borders and can catch thieves attempting to conduct operations in your province.

- % * 2.0 Chance of Catching Enemy Thieves

- Reduces damage caused by Enemy Thieves by % * 2.5

#### Universities

Universities increase your scientist generation rate and allow your scientists to produce books more effectively.

- Increase spawn rate of new scientists by % * 1.5

- % * 1 Higher Generation of Science Books

- Not affected by Building Efficiency

#### Libraries

Libraries increase Science Efficiency.

- % * 1 Higher Science Efficiency

- Not affected by Building Efficiency

#### Stables

Stables are the buildings where your peasants breed your war horses, strong horses sent in combat and increasing the offensive strength of the troop mounting them. Nevertheless, horses do not participate in defense, and you obviously cannot send more horses in combat than you have actual troops!

- Produces 2 Horses Per Day

- Holds 80 Horses

#### Dungeons

Prisoners caught in combat are held captive in your dungeons. A dungeon can only hold a limited number of prisoners.
While imprisoned, prisoners will be assigned to province duties, providing you some extra gold. For more detailed information on how much gold they generate, please go to Economy for the income formula or go to Military for an additional definition of Prisoners.
Deserting troops will fill dungeons first, if any space is available, before being completely lost.

- Houses 30 Prisoners of War

### Retired buildings

- Shipyards: 1.5% chance of creating a boat, holds 5 boats per shipyard. 1 boat was needed per 100 troops sent to attack someone on another island.

- Taverns: Lowered Draft costs and Mercenary costs.

- Plazas: Employed extra Peasants.

- Strongholds: Increased OME (now Training Grounds).

- Mines: Produced a certain number of gold per acre.

- Schools: Increase production of Science Books.

- Laboratories: Increase scientist spawn rate.

- Guard Stations: Decreases Land and Resource Losses when Attacked by % * 2

### Construction

#### Construction Time

**Construction Time =** 16 * Racial Mod * Personality Mod * Builders Boon * Double Speed * War Bonus * Ritual Mod * Artisan Science Mod

Modifier Type | Active | Otherwise
--- | --- | ---
Builder's Boon | 0.75 | 1
Double Speed | 0.5 | 1
Double Speed in Protection | 0.75 | 1
Ritual: Haste | 0.75 (at 100% efficiency) | 1

Note that construction speed is rounded at .5 That means if the build time is 15.49, then it is rounded down to 15. If it is 15.5, it will be rounded up to 16. For a double speed build, assuming normal construction is 15.49, the speed build time will be 15.49/2 = 7.745 = rounded up to 8 hours. For 14.9 though, it will be 14.9/2 = 7.45 = rounded down to 7 hours.

#### Construction Costs

**Construction Costs =** 0.05 * (land + 10000) * Race Mod * Personality Mod * Mills Mod * Double Speed * Ritual Mod * Artisan Science Mod

Modifier Type | Active | Otherwise
--- | --- | ---
Double Speed | 2 | 1

#### Raze Costs

**Raze Costs =** (300 + (0.05 * land)) * Artisan Science Mod * Race Mod * Personality Mod

### Buildings

#### Building Efficiency

**Available Workers         = ** Peasants + *ROUNDDOWN* ( Prisoners / 2 )

**Optimal Workers           = ** *ROUNDDOWN* ( Total Jobs * 0.67 )

**% Jobs Performed          = ** *MIN* ( Available Workers / Optimal Workers *,* 1 )

**Building Efficiency       = ** (0.5 * (1 + % Jobs Performed)) * Race * Personality * Tools Science * Dragon * Blizzard

- The "Current Available Workers" value, provided by the Internal Affairs Adviser page, already takes prisoners into account.

- Building Efficiency affects ALL Flat Rate and Percentage-Based buildings.

- Building Efficiency has NO effect on Capacity component of Capacity Buildings.

- Changes in Building Efficiency take effect gradually.

Modifier Type | Active | Otherwise
--- | --- | ---
Race: Dwarf | 1.30 | 1
Dragon: Topaz | 0.75 | 1
Spell: Blizzard | 0.9 | 1

#### Building Effects

**Percentage Based Buildings =** Base Effect * BE * MIN(50%, % of building * (1 + Race)* (1 + Personality)) * (100% - MIN(50%, % of building * (1 + Race)*(1 + Personality)))
**Flat Rate Buildings =** Base Effect * Number of Buildings * (1 + Race) * (1 + Personality) * BE

- In general, the Max Effect of a %-Based Building is 25 x Base Effect (exceptions apply, refer to table)

- If your BE is less than 100%, the effect you would have with 50% of that building is the maximum.

- If you have less than 100% BE, additional buildings past 50% will have no effect.

### Changelog

- Age 107: Updated Building Effects formulas to include personalities.

Buildings
---
Civil Buildings | Barren Lands  •  Homes  •  Farms  •  Mills  •  Banks
Military Buildings | Training Grounds  •  Armouries  •  Barracks  •  Forts  •  Castles  •  Hospitals  •  Stables  •  Dungeons
Thievery and Mystic Buildings | Guilds  •  Towers  •  Thieves' Dens  •  Watchtowers
Science Buildings | Universities  •  Libraries

## Bushels

**Food** is a resource, and it is needed to keep population of a Province alive. It's measured in **bushels**.

### Food Consumed

**Bushels Eaten** = Total Population * 0.25 * Race Mod * Gluttony Mod

Modifier Type | Active | Otherwise
--- | --- | ---
Race: Undead | 0 | 1
Race: Dwarf | 1.5 | 1
Spell: Gluttony | 1.25 | 1

- If a province has zero food, it will enter into a state of starvation. While a province is starving, its population (peasants, military units and thieves) will die off at a rate proportional to the food deficit (this also includes armies away from home). Wizards are not affected. This rate is capped at 5% and will continue until the province has a value for food greater than 0.

### Food Produced

**Base Food Production     =** ((Farms * 60) * Building Efficiency) + (Barren Land * 2) + (Race Mod * Acres) + (Personality Mod * Acres)

**Modified Food Production =** Base Food Production * Production Science Mod * Fertile Lands Mod * Drought Mod * Honor Mod

Condition | Modifier
--- | ---
Fertile Lands | 1.25
Drought | 0.75

### Food Decayed

**Food Remaining** = Food Stock * 0.99 + Modified Food Production - Bushels Eaten

0.99 or about 1% of the total food stock decays in normal conditions. The exact amount depends on the modifiers in the formula as provided above and it is calculated on the total food stored in the province. So if a province has 300,000 bushels of food in stock under normal conditions, then the expected decay is slightly less or more than 3000 bushels per tick / Utopia day. There may be scenarios where the total food decayed, is higher than what remains after food needed by the population is consumed from the food grown. This may lead to depletion of the stock in the province especially after a war when the people are much lesser compared to the maximum population limit and the stored food may be much higher or when a new player has built a lot of farms / received aid as food. This will normalize once the population reaches back to expected levels and the province only needs to ensure that the food grown is more than the food needed by the population at all times so as to avoid starvation.

## Chaining

This is part of the Utopia WIKI Player written guides.
---

THIS PAGE is a guide aimed to cover Chaining. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page. | THIS PAGE is a guide aimed to cover Chaining. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.
--- | ---
THIS PAGE is a guide aimed to cover Chaining. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.

### Contents

- 1 Full Chains When...

1.1 Target has armies home
1.2 Target has armies out for a few hours
1.3 Target has armies out for several hours

- 2 Semi Chains

### Full Chains When...

#### Target has armies home

*If the target has armies home, you get to land lock him. With no incoming acres to save him, he will have so many peasants/wizards (can't get rid of peasants and wizards easily) per acre that he can't release and hit.*

Advantages | Disadvantages
--- | ---
You're certain to cause his offense to desert. | This is very difficult to do if he uses elites. Even against strength 2 elites, the extra defense does a lot to prevent doubling.
Peasants don't start leaving before his offense starts deserting, letting him stay high on peasants longer. | The desertions cause massive NW drop since his offense leaves too, so you need to hit massively in 1h, at most 2h, meaning that you can't take advantage of defense desertions.

#### Target has armies out for a few hours

*If the target's armies arrive in a few hours, we get to do the same as above with his military out, allowing for easier doubling. The problem here is that his armies will typically bring back land. While 200 acres is what we'll take on a single hit early in the chain, it can easily amount to 4-5 hits later in the chain. If we put the target at 200 acres and armies return home with another 200, he gets to double his size and keep roughly twice as much offense. Meaning that our worst defended province has to be twice as big to stay safe.*

Advantages | Disadvantages
--- | ---
His armies are out, allowing for much easier doubling. | If his armies bring back acres, several of our final hits will be neutralized.
Offense desertion starts about the same time as peasants start leaving, meaning more time for desertions before the peasants are gone. | We won't have as much time for it, if people are late they miss out entirely.

#### Target has armies out for several hours

*If the target's armies were just sent out, the situation changes a bit from the second case. A lot of desertion will happen while the army is out, meaning defense desertion only. Since his offense doesn't desert, his NW will stay high. This allows us to wait for defense to desert before finishing him off, doubling more easily.*

Advantages | Disadvantages
--- | ---
If we have a large spread, we will be able to make quality hits more easily by waiting for desertions. | His peasants start leaving a while before his offense starts to desert, meaning less time for offense desertions.
 | As in the above case, it's a big problem if his armies bring back many acres.
 | With a small spread, we can't really take advantage of the desertions as they drop the target's NW below our line of attackers.

### Semi Chains

So your kingdom networth is relatively larger than your opponents, and you'd like to control their economy and ensure that you gain the upper hand at the top.
Thus, you choose to semi chain them, whilst aiding up unbreakable provinces. Winner!

## Creating a province

Before you can venture into the world of Utopia, you must first create a province. Players are only allowed to create one province per server.

### Contents

- 1 Creation

- 2 Activation Email

- 3 Restrictions

- 4 Protection

- 5 War

- 6 Science and Books

#### Creation

To create a province, select a server (i.e. World of Legends) and, if a province has not already been founded, you will have the option to create a new one.
The following information is required:

- Name of province (max 30 characters and contain only the following characters: a-z, 0-9 and "space")

- Name of the province's leader (max 20 characters and contain only the following characters: a-z, 0-9 and "space")

- Leader Gender

- Desired Race

- Speciality

#### Activation Email

This email allows the player to activate their province which is required in order to continue playing. Players may request a new activation mail if they did not receive or misplaced the original.
Sample Activation email:

Thank you for joining Utopia.  For security reasons, please verify your email address by visiting the following URL:
http://utopia-game.com/shared/email_verification/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
This account must be validated by Sat, 4 Aug at 14:04 GMT+00:00 or the account will be deactivated.
If you did not sign up to Utopia (utopia-game.com) please ignore this email and the offending account will shortly be deactivated.

#### Restrictions

If you recently abandoned a province, you will be unable to create a new one. You must wait 24 hours before attempting to create a new province.

#### Protection

For a period of 24 hours, new provinces are placed under protection. This prevents other players from attacking and allows you to build up resources to aid against the oncoming slaughter. Provinces are not able to send Aid, change the Wage rate, cast on Rituals, fund or slay Dragons while under protection. However, if the kingdom the new province is created in is at war, the protection period will last 3 real-life days instead of 1.

#### War

- Provinces created/reset during War will start without
 Soldiers
 Military
 Building Credits.

#### Science and Books

- Provinces created late now start with some books based on the time created during the age

- Each category will get an equal amount of books equivalent to 1/3 of the total books the province should start with

- Total books a province should start with is 85% of the amount of books that would be generated by the amount of scientists (Recruits) the province is starting with to that point in the age

- Starting scientists for a late starting province is increased by days into the age divided by 3 for each day after the 3rd day into the age.

## Dual Monarch

This is part of the Utopia WIKI Player written guides.
---

THIS PAGE is a guide aimed to cover Dual Monarch. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page. | THIS PAGE is a guide aimed to cover Dual Monarch. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.
--- | ---
THIS PAGE is a guide aimed to cover Dual Monarch. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.

Dual monarchy is a system employed by some kingdoms, whereby votes are split between two provinces. Normally, these provinces are trusted players and/or leaders of the kingdom that can be counted on to be active.
The way this system works is that if **Province A** and **Province B** are meant to be sharing votes with **Province A** being the main monarch, then each province would vote for the other, and **Province A** would ensure that he gathers enough votes on himself to be the monarch. When **Province B** requires monarchy however, he will switch his vote from **Province A** to himself and thus gain the monarchy.
However, this may lead to the kingdom page showing 2 monarchs present in the kingdom until **Province A** is updated.
In previous ages, these votes were shared between the real leader and a large province during wars to create an unbreakable province due to the +10% Defense bonus conferred to monarchs in War/Hostiles. This bonus is no longer active though.

## Economy

### Contents

- 1 Money

1.1 Raw Income
1.2 Modified Total Income
1.3 Military Expenses / Wages

- 2 Population

2.1 Total Population
2.2 Current Population
2.3 Peasants

2.3.1 Hourly Change

2.4 Employment

2.4.1 Available Jobs
2.4.2 Unfilled Jobs
2.4.3 Employed Peasants
2.4.4 Unemployed Peasants
2.4.5 Employment Rate

Money
**Gold Coin** (1gc or $1) is Utopian Currency, the base of Utopian Economics.
Banks and population produce money, wizards could cast it from Tree of Gold.
Spend money on Exploration, Building, Training, Wages, Dragons or aid your teammates.

#### Raw Income

**Raw Income =** (3 * Employed Peasants) + (1 * Unemployed Peasants) + (0.75 * Prisoners) + Racial Gold Generation + (Banks * 25 * BE) + Miner's Mystique Gold Generation

#### Modified Total Income

**Modified Income =** Raw Income * Plague * Riots * Bank % Bonus * Income Sci * Honor Income Mod
                  * Race Mod * Personality Mod * Dragon * Ritual

#### Military Expenses / Wages

**Military Expenses = **(((Def specs + Off specs ) * 0.5) + Elites * 0.75) * Wage Rate * Armouries Bonus * Race Mod * Personality Mod * max(Inspire Army , Hero's Inspiration) * Greed * Ritual * Dragon * Bookkeeping Science Effect

**Note**

- Wages are not paid to basic soldiers

- Greed affects provinces as a wage penalty, not an income penalty

Population

#### Total Population

**Raw Living Space =** ((Built Land + Land in progress) * 25) + (Barren Land * 15) + (Homes * Homes Capacity)

**Mod Living Space =** Raw Living Space * Race Bonus * Population Science * Honor Population Bonus

**Note**

- Honor Bonuses are calculated as 1 + (Personality Mod * Honor Bonus)

#### Current Population

**Current Population =** Peasants + Soldiers + Off Specs + Off Specs in Training + Def Specs + Def Specs in Training
                     + Elites + Elites in Training + Thieves + Thieves in Training + Wizards

**Note**

- Prisoners do not add to the population

### Peasants

#### Hourly Change

**Peasants Hourly Change =** (Current Peasants * ((Birth Rate + Love & Peace) * Race Bonus * Hospitals Bonus * EOWCF * Chastity - Storms)) + (Homes bonus * Chastity) - Drafted Soldiers - Wizards Trained

Modifier Type | Active | Otherwise
--- | --- | ---
Love & Peace | 0.85% | 0
Storms | 1.5% | 0
Chastity | 0.5 | 1

**Note**

- Base birth rate is 2.05% and ranges from 1.9457% up to 2.1525% (± 5% of 2.05%)

- Base birth rate is increased to ~3% during Protection

- There must be enough population space for peasants to increase

- When a province is overpopulated, the number of peasants will decrease by 10% per tick

### Employment

#### Available Jobs

**Available Jobs =** (Completed Buildings - Homes) * 25

#### Unfilled Jobs

**Unfilled Jobs =** *MAX* ( Available Jobs - Peasants - *ROUNDDOWN*( Prisoners / 2 ) , 0 )

#### Employed Peasants

**Employed Peasants =** *MIN* ( Peasants , Available Jobs - (*ROUNDDOWN* ( Prisoners* / 2 )) )

**Note**

- Prisoners are included in the Employed Peasants calculation for Building Efficiency. Prisoners are not considered actual peasants, as they do not generate the same amount of gold as employed or unemployed peasants (they only generate 0.75 gold regardless of employment)

#### Unemployed Peasants

**Unemployed Peasants =** MIN(Peasants - Employed Peasants)

#### Employment Rate

**Employment Rate =** (Employed Peasants / Peasants) * 100

## Ethics of Waving and War

By W1nd. 12-12-2020. Part of Utopia News, Age 88.
Original: http://forums.utopia-game.com/showthread.php?640067-ETHICS-OF-WAVING-and-WAR-(UTOPIA-NEWS-AGE-88)

### Contents

- 1 WAVING vs. DIPLO

- 2 ETHICAL MATTERS

- 3 TO PK, or not to PK

- 4 WHEN TO WD

- 5 RAZING INTO WARS

#### WAVING vs. DIPLO

Now, there are two waves of achieving war in UTOPIA. There are two schools of belief when it comes to this; waving for war and diplo. Most people like arranged wars because it gives everyone plenty of time to get ready and it is like showing up for work. Everyone knows what time to login and when to be ready to use their consumables (stealth and mana), very easy to plan your day around these wars. Typically they are referred to as “arranged wars”, which always get scrutinized closely by the community as everyone is extremely paranoid about war fixing and ‘fake wars’ which no one likes to hear about. In my mind I do not really see an issue with this but it is not my preferred method of getting war, it is however easier for people with a busier schedule and those not comfortable with certain elements of the game (no dragons). I believe setting limitations takes away from the game but that is just me.
Waving for war is my preferred method and I wish everyone did it more often, too many kingdoms hide in their shells and are far too reactive. One of the most important things is waving out during your OOW period not just for plunders but for books as well! The downsides to waving for war is that you never really know when the enemy may declare, but they do still have to march several armies just to get the war button. Anyone paying attention to their bot will get a notification that a province was attacked or at the very least the province ruler will see it and would be best to notify their LS (leadership) as soon as possible. There are virtually no restrictions or diplo required but it can be added as an extra layer if you so choose.

#### ETHICAL MATTERS

I wanted to take this time to touch on some ethical matters within the game as well when it pertains to warring since we are already on the subject.

#### TO PK, or not to PK

This is a sticky subject, there is not really a ‘right’ way or time to do this but sometimes it is needed. Typically only a few things would generate enough resentment towards a province to commit the act of a pk; dragging wars, explicit in game mail, explicit dm’s in discord, and more commonly a vendetta that will never be dropped like we saw with Princess Jasmine and gv, I doubt that will ever end based on what I heard from Jasmine regarding gv. Notwithstanding, they have made it significantly harder to PK a province, however is not impossible, I feel it is just a waste of time in any case. There will always be a better attack. Bottom line, if you get Pk’d, it is likely you just neglected your province for too long or you or your kingdom did something to bring it upon yourself.

#### WHEN TO WD

Most monarchs will tell you that when the NW/ACRE gap reaches a certain point by min time that is a good indicator that you stand to lose more than you could possibly gain. The winner of the war always gets propelled to the top of the charts in one way or the other especially this early in the age. There is strategic value in this however as you can push your kingdom down lower in the charts by holding out on withdrawal, which means more targets and possibly a faster war since there will be many more options. What I hate to see is when the LS or Monarch is ‘punishing’ their kingdom for something they did or did not do. Most monarchs will concede once they can no longer see a clear path to victory. This at the end of the day is very subjective and without knowing the full story/strategy we can only make assumptions based on the limited game data we have access to as spectators.

#### RAZING INTO WARS

Unless you want a severe beatdown that could potentially cause you to rage quit or destroy your entire kingdom, I would avoid this behavior. The community is generally very accepting of mistakes and errors but when things are done maliciously it is not cool and no one deserves to be harassed in a game that is meant to be fun for all. I feel strongly that this aspect should be blocked from the game, I know others feel the opposite but this would solve a lot of the butthurt grudges by not allowing them to continue. Secret alliances can also influence wars by razing provinces to help the other team, not to mention sending override dragons. For these reasons alone I would call these acts interference of the mechanics of the ‘war’ and secret collusion with the opponent resulting in a fixing of the charts.

## Exploration

Exploration is one of the main ways of growing your Province. Via the Explore page, a province may send out soldiers, at the cost of gc, to acquire additional acres.
On this page you will have the following information:

- Exploration Costs (Soldiers)

- Exploration Costs (Gold)

- Available Uncharted Acres (also known as the Explore Pool)

- Currently Exploring

- Maximum Explorable Now

If you have the Soldiers and the Gold, you will be able to explore for Acres to grow your Province. Explore costs increase significantly when over Kingdom Median in acres.

### Available Uncharted Acres

Available Uncharted Acres, also know as the Explore Pool, has the following features:

- Starts at 200 Acres at the start of the Age.

- It grows by 2 Acres per Tick.

- It is soft capped at 1000 Acres.

- When a War ends, a provision of additional Pool is added to each Province for both Kingdoms.

- Each Province will have 5% of their Land removed and added to their Explore Pool (minimum of 100 Acres added to Pool, regardless of how many are lost).

- Pool Acres over the soft cap of 1000 Acres at War's end are added to land .

### Restrictions

The following restrictions are in place:

- Provinces may not explore without the resources to cover the costs.

- At least 50% of existing Acres must be built or undergoing construction.

- The Explore Pool must be greater than 0 Acres.

- Provinces can not explore more than their current Acres at once.

- Kingdoms with less than 10 Provinces will have an explore penalty.

#### Effects of War on Exploration

The following penalties apply during war:

- Exploration costs increased to 600% during active War and End of War Cease-Fire (or 300% during End-of-War Cease-Fire for Provinces below the Kingdom Median, including incoming explored Acres).

- During End-of-War Cease-Fire, when under Median, explore time is reduced by 50%.

## Explore Pool

The Explore pool is a pool of acres available to each individual province in a kingdom to use for exploring. This pool begins at the start of the age at 5000 acres and grows by 100 acres each hour. The pool decays, while not in war, at .5% an hour.

## Finding Good Learn Targets

This is part of the Utopia WIKI Player written guides.
---

THIS PAGE is a guide aimed to cover Finding Good Learn Targets. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page. | THIS PAGE is a guide aimed to cover Finding Good Learn Targets. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.
--- | ---
THIS PAGE is a guide aimed to cover Finding Good Learn Targets. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.

Just like any other target finding, start taking SoT's of provinces hopefully in your networth range (I'd say no further than 95-120% your networth). From the SoT you're looking at a few things in particular to get a grasp on sciences they may possess before SoS'ing them.
1 BE if they have greater than 100% BE other than dwarves they have tools science the higher the BE the higher the science.
2 Population is one of the more important science and usually can be seen in full on the SoT, some wizard/thief heavy provinces show lower than full.
Base ppa for each race:
Faeries = 23.75 ppa
Everyone else = 25 ppa
Undead = 28.75 ppa
If they have better population than this they are one of 3 things running homes, above Lord honor title, or have some amount of science. The ones with larger ppa's are who you want to look at.
SoS these guys to get their science percentages.
3 Persona, always SoS a Sage when you see one you never know how much they will have in science. Especially if they have some amount of elites.
Get an SoS infact I would have yourself narrowed down to 3-4 targets, from the SoS figure out how many books per acre they have roughly. Pick the one less likely to retal you and also the one with the most books per acre in the science you are focusing on. Typically focus on one science at a time, if they have only 1 or 2 sciences you will gain better on them than if they have all 7 sciences. - Uzziah

## Finding Good Plunder Targets

#### Finding Good Plunder Targets

- Finding a good plunder target is easier than it seems. There are a few things that you need to look for:

- Networth Per Acre(NWPA)
 A low NWPA usually indicates a low military drafted province with a stronger economy. This will mean this province has a lower defense and potentially more resources on hand.

- Networth Range
 When attacking a province in general, Networth Range always plays a factor. The farther you are outside of the networth range the less your gains will be.

- Personalities and Races
 Look for a province that is of the TM race. Usually rogues will stock up on resources since it is harder to break and steal from them.

- Exiting War
 Look for kingdoms that recently have left war. You can utilize the bot by typing ".plunders" and it will show which kingdoms have left war stance within the past 6 hours. Sometimes you can get lucky and catch a province that missed their training date and still is stocked with resources.

- Rankings
 Kingdoms within the top 15 of rankings usually have a few provinces that stock resources. Do remember though, you are playing with fire when and if you decide to mess with any top kingdom. They could raze you back, retal, or full on wave your kingdom.

Just remember, there are consequences to your actions and need to play smart when it comes to plundering.

## Freeze time

This is the time at the start of every age, before Protection begins. During this time you may log into your province and navigate the game, but the games time will not progress. This time is to allow players to decide on a kingdom strategy or races and specialties. During Freeze time you may reset your province details from your Preferences menu.

## Getting Started with Utopia

### Contents

- 1 Role & Style of Play

- 2 Race & Personality

- 3 Buildings

- 4 Arts & Sciences

- 5 Military

### Role & Style of Play

In Utopia, focusing on a clear role helps shape your strategy. The four main role categories are:

Thieves | Mages | Attackers | Hybrids
--- | --- | --- | ---
Masters of stealth and covert operations    Specialize in:  Eliminating enemy troops silently    Economic sabotage    Propaganda campaigns    Excel at gathering intelligence    The **Rogue** personality enhances their abilities | Wield powerful Arcane magic    Cast spells that:  Strengthen your province    Weaken enemies    Wizards are acquired gradually, not trained directly    The **Mystic** personality boosts mage guilds and grants special spells | Focus on military might and aggression    Launch attacks to:  Capture enemy land    Destroy enemy buildings    Massacre thieves, wizards and peasantry  Ideal for players who prefer direct combat | Combine two roles for flexible strategies:    Attacker/Thief (AT) — stealth + aggression    Attacker/Mage (AM) — magic + force    Hybrids create well-rounded provinces capable of adapting to many situations

### Race & Personality

Choose Races and Personalities that fit your preferred role and playstyle. Small bonuses accumulate into major advantages over time.

### Buildings

Build strong infrastructure to support power and growth. Peaceful development often complements military strategies.

### Arts & Sciences

Invest in science for steady, long-term bonuses. Though subtle initially, these benefits grow and provide valuable advantages.

### Military

Balance troop drafting and wages carefully to maintain a strong defense without harming your economy. Collaborate with kingdom allies to improve your military strength.

## Guide

Growth

If a kingdom is optimizing for growth, always ask your monarch before you take acres from the explore pool or cast paradice.
If you are dicing for growth, you want about 20-25% guilds and as many towers as necessary to cast the spell every tick. If you are exploring for growth, it depends on how you?re doing it, but you?ll want mills and banks and potentially armories to bring down the draft cost. However, for most provinces that you would want to explore, peasants generate more gc than the tb hit from getting aided soldiers so trading is more optimal where you can afford to buy soldiers for TB and get them aided instead of drafting..
Most provinces will grow largely from attacking. Which leads us to -- how do you grow from attacking?
The answer is partly that it depends. There is one central rule, however:
THE BEST WAY TO GROW IS TO NOT GET RETALLED.
Your province will be in the best possible shape if you acquire safe acres and don?t get retalled. Even if you only get 50 acres per hit when you could get 150 elsewhere, this is the best way of growing. Why? Because every so often the hit for 150 might get you hit back for 250, then you?re trading hits and dealing with military/peasant loss that is bad for your province.
Generally speaking, when you?re whoring, you want to be focused on offense to the exclusion of defense to bring down your nw relative to your targets and let you hit safely. This is part of why you need to be disciplined when whoring -- two ages ago, I whored up to 6k acres with under 6k defspecs and pure offense elites. Growing this way is more art than science; unfortunately you need to have an understanding of whether you?re likely to get waved and if you are, you need more defense. So it?s not something you can do without some kind of deals.
So how do you identify safe hits? First, you look at the province you?re hitting - what?s their OME? If it?s higher than honor + payrate, they have TGs and are an attacker. This means be careful. Do they have horses? Another sign of an attacker. Generally speaking, attackers can hit you back which is what makes them bad hits -- it costs you or your kingdom acres when they hit you back. You want to hit t/ms that are the biggest province in their kingdom in kingdoms with no attackers the same size as you / in range to retal your kd.
Now, obviously this is more of a general rule than hard and fast; it?s impossible to always hit safe provinces, but always hit the safest in a kingdom if you?re randoming a kingdom, and always hit the safest available to you.
When growing, a sample build might be something like:
8% farms
16% TGs
25% guilds
5% towers
10% stables
20% banks
15% hospitals
1% dungeons
The goal here is to have decent econ (banks/hosps), offense (TGs/stables), and still gain WPA.
I got hit, what do I do?
Generally speaking, if you got hit you can't hit back. If you can, you should. Retalling slows growth at the top and generally discourages more hits into your kingdom. There are some issues here though -- eventually, target selection reaches a point where you're the most attractive target even if you do retal. And sending out can get you hit more. So you need to have a sense of what else is out there that can be hit.
In ~95% of situations, retalling is the right move for you to make.
If you can't retal, there are some ops you can do, but generally the best move is to rob resources from the kingdom that hit you.
Generally speaking, training offense will make you less likely to be hit (by bottomfeeding SKs) than training defense. It's more NW efficient and makes hitting you risky.
Waving for Acres
There will be times when due to setup, global growth mechanics, or cf?s purely safe whoring is not viable. At times like this it is possible to hide your weak whoring ability by running a more war-growth hybrid build and wave kd?s that you believe are unlikely retal. If you random out on a bad hit, then you are much more likely to be retalled than if you wave a kd. However, this is still a far more risky option than safe whoring. This can be a good strategy for when you have a combination of turtle core and suicide core. Knowing when you can get a war from waving, when you will get a cf and acres from waving, and when you will be trapped getting fb?d for weeks is critical to this more risky strategy.
Pumping
When pumping, again, you need to have an understanding of the climate. If you?re not likely to get waved, you can pump more aggressively than if you are likely to get waved. When pumping, you generally want to get to whatever the set ?target? defense is, and then have as many peasants as possible. You will need thieves and/or WTs to protect from being robbed.
Scipump
When pumping science as a TOG race, a sample build would look something like:
8% farms
22% guilds
35% banks
30% schools
5% towers
Note -- you only want as many towers as it takes to TOG. You want ~15% guilds minimum; we generally prefer to run more (even more than the 22% here) to pump WPA at the same time. The schools/banks distribution is something that will vary as you gain more alc sci and BE sci, but this is a decent starting point.
You?d generally be hoping to achieve about 8 military units/acre, 2 TPA, 2 WPA, and 15 peasants/acre, give or take.
Elitepump
An elitepump would look similar to a scipump, except you wouldn?t have schools and would probably have all banks until you want to start drafting. Then you would rebuild to have 25-30% arms, (more/less depending on cost) and train them all in one go.
Homespump
A homespump operates similar to an elitepump. The main difference is that ~48h before you begin drafting, you rebuild to add homes to your build -- the number of homes depends on how much gold you have available. This lets you draft from a higher population number, meaning that when you raze the homes, a higher % of your total population will be in military compared to not using homes. Using homes can be a very effective way of getting drafted quickly or getting more drafted than you could have without homes.
WPApump
This is pretty basic -- run as many guilds as you can. At least 50%, preferably more.
Kingdom Tools
If you use any of these, design any of these, and want to add a little, please let me know.
There are some general tools available for use. There is utopiapimp,and upoopu that are publicly available, and then stinger makes stingernet available and munk makes munkbot available. Lucidbot is an IRCbot that is also publicly available.
Utopiapimp
This is the most basic of the sites. It does not link with an IRCbot, or as far as I know, have a browser extension. Forum agents(such as the one included in Angel) can send directly to it. You can then view data on your kingdom or opposing kingdoms along a number of different metrics. The way intel can be viewed is highly customizable on utopiapimp. It can also track ops, which have to be inserted manually into it. Utopiapimp sometimes suffers from display bugs.
upoopu
A more optimized webtool that has similar data to utopiapimp. It has a browser extension which makes it easier to get data into the system. It is supposed to be easier to manipulate data once it is in the system as well.
Stingernet
Stinger makes stingernet available. It is an ircbot that is linked to a website. It has similar data available in its website. It also has a custom targetfinder that is linked to a NAP system to prevent anyone you have a CF with from showing up in the targetfinder. In order to have access to stingerbot/stingersite you must obtain permission from Stinger. There are limited spots for his service. Stingernet is largely available on the absnet server, although it has migrated to utonet on some kd?s. Having an ircbot means that you can enter a command string, such as !cb zauper and get back my SoT, rather than having to go to the website to view it. It?s partly a matter of convienence, and partly very helpful because there are custom views that are easier to get on IRC than through the website -- a sci calc, for example.
Stingernet also includes an automated WPA calculator.

- I?m told that Stinger currently has it available now.

Munkbot
This is what CR uses. It has similar features to stingernet, listed above, plus a number of other ones. It includes an activity tracker (internal and external), links to prep and province simulators to help you prepare for conflicts or think through strategy, and has fully customizable views that are designed to be exported into other tools for setting up waves. It is both a website and a bot.
It also tracks op success rates over time and will automatically calculate WPA for provinces you collect all intel on. (You can force it with !wpacalc on IRC).
It also has incorporated tools similar to utools below.
You can also generally request a feature from Munk and he will code it after spamming !donate at you for a few minutes. He?s fussy but if you ask nicely he?ll probably set up a bot/site for you.

IRC Bot:
orders
aid
tracks ops
tracks attacks
show intel
integrated with whatsapp and can call/sms.
perform calcs (soldswap / wpacalc / defence home / practical offence / offense keeping set defense and much more)
Lucidbot
Lucidbot is only a bot. It collects intel from whatever repository you use and is fully customizable for reporting. It comes with many of the same bot features as stinger/munkbot. Lucidbot must be hosted by someone in private channel. Lucid is very easy to obtain and can be used in conjunction with any of the other public intel sites such as pimp or upoopoo. An intel depository site and intel pull script has been in the works.
Other Tools
Angel
Angel is the classic tool for intel. You take a SoT, copy the intel, there?s an export line so anyone else with angel can read it in. Angel forum agent can be used in conjunction with all bots and intel repositories that lack intel-pulling scripts.
utools
A browser extension that duplicates much of angel?s functionality. Alters UI in-game, adding features such as expected gains and beheading advisors.
Targetfinder
Munk?s targetfinder (tf.umunk.net) is probably the best publicly available targetfinder. To use it, search for provinces within your nw range (+/- 30% nw), you can set kingdom size restrictions as well, and sort/limit by race. The TF also possess war trackers. Site is sometimes private at start of age.

Overpop
Note: preventing overpop is a mechanic that really privileges activity and it is not expected in most kd?s that you do these things when being chained. If you do nothing else but mass LL before troops get home so as to be able to send out easily this is still better than nothing. However, lots of wars are won or lost by how successful chains are, and these things make chains fail. One of the most significant differences between top-tier kd?s and standard war kd?s is their commitment to overpop control and maintaining a strong ?small? group of provs.
So, a few new things to work on for preventing overpop. Preventing overpop as you go down in a chain is good for lots of reasons: 1) if you have enough land coming in with armies you end up losing nothing and the chain is completely useless, 2) without losing defense you are able to maintain higher def, often preventing multi-taps which can also decrease chain success. 3) At the bottom of a chain defense is, perhaps counterintuitively, often more valuable than offense.
So the basics are still the same: have lots of acres incoming, army-in army-out, release to dragon if you have to before sending out. Here are a few formulas and tricks though:
Military desertion formula: ((((total pop-(peasants*.07))/maxpop)-1)/5) * (thieves + eliteshome + soldiershome + specshome)
Note: You only desert if maxpop*1.15 is less than totalpop-(peasants*.07). So if you have 10k total pop and 9k maxpop, you?re not deserting.
You lose up to 7% of your peasants/tick when you?re overpop, and they leave prior to desertions which is why the formula includes that.
If this number is equal to the amount of soldiers you have, you only lose soldiers for the tick. This is why pers/race bonuses that return dead troops as soldiers are are so valuable when lots of people use IRC, because you use the soldier pool to prevent casualty losses. A good kd will use the soldiers generated to try to bounce provs and feed others. A great kd will use the soldiers to make it as if the prov was never chained in the first place.
Trick #2: besides microing tickly loss this way(either by releasing thieves into soldiers to leave, being aided, ect) another strategy to alievate the destruction of chains is to setup LL targets, either via AW or out of control growth. These target should not be targeted by attacks and will serve exclusively as LL farms for chained provs. The only spell not affected by -damage mods in race is LL damage, so regardless of what kind of attacker you are, if you are likely to be chained you should try to maintain 60 mana at all times. That's a lot of LL, and the target will always be very large, and have no wpa. When your land is about to come in, LL to where you would need to be once acres come in + are built and then go use your great new mwpa for fb.
People argue over the value of releasing WPA on chained provs.
1) If you keep the WPA, you wind up with high WPA provs capable of FBing potentially otherwise unoppable provs in the other kingdom
2) If you keep the WPA, you wind up with a lot of lost potential military and your chained provs potentially fall behind
3) If you release the WPA, you can LL less (but you would run out your mana on LL before releasing
4) If you release the WPA, you can be intra-kd fireballed to release peasants, but it usually is better to release the WPA (several ticks) prior to army coming home, as you release WPA into peasants that you then need to lose to solve overpop.

## Guide Combo Selection

This is part of the Utopia WIKI Player written guides.
---

THIS PAGE is a guide aimed to cover Guide:Combo Selection. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page. | THIS PAGE is a guide aimed to cover Guide:Combo Selection. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.
--- | ---
THIS PAGE is a guide aimed to cover Guide:Combo Selection. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.

Your Race and Personality combo is extremely important. It will affect how you play Utopia and what spells and thievery ops you have available to you. To decide what Race and Personality bests suits you first need to select what role you will play in the kingdom. Will you play as a full out attacker, will you take the indirect route and put your resources into thievery ops or magic. Quite often you will work with your kingdom and other players to provide cover in areas others are lacking.
There are a wide but set variety of possible playing styles, each with its own strengths and weaknesses. All are discussed here in very limited detail. All recommended combinations are simply that - recommended. There is no such thing as a "wrong" combination of race and personality (however, there are inefficient ones) and all players should play as they feel comfortable. If unsure, ask a kingdom-mate or friend to help you decide. It is always a good idea to ask for advice and input from your kingdom when it comes to deciding what you're going to focus on in the coming age.
Before dipping (albeit broadly) into the choices available to a newcomer it is worth mentioning two almost conflicting virtues of Utopia- It is illegal and wrong to be forced to choose a certain style, theme, race or personality by your king, kingdom or alliance. You don't have to do what you don't want to do. Yet even so, you should remember that Utopia is a team-based environment and there is much to be said for the pride and pleasure earned from having a united theme or an organized group of attackers. The balance between being an individual and playing for the kingdom is one that is addressed in the decisions you and your fellow kingdom-mates make every day. It is up to you how to view that balance.

### Contents

- 1 Utopia Province Role Types

1.1 Pure

1.1.1 Attacker
1.1.2 Thief
1.1.3 Mage
1.1.4 Warning

1.2 Hybrid

1.2.1 Attacker/Thief
1.2.2 Attacker/Mage
1.2.3 Thief/Mage
1.2.4 Attacker/Thief/Mage

1.3 Explorer/Bank

### Utopia Province Role Types

#### Pure

##### Attacker

Any players that exclusively attacks enemy provinces is known as an attacker. This is done through the War Room page, and allows the attacker to take land and other resources from enemy provinces. Attacking is the most common style of play, and almost any race is capable of attacking effectively, with the Warrior and Tactician personality most often cited as useful personalities to accompany an attacking player.

##### Thief

As intended here this playing style would be better off known as "pure" thief or "superthief", in that they are not capable of attacking, nor are they generally able to perform concerted magical offenses. Their sole expertise lies in thief operations such as Nightstrike and Kidnapping. The Halfling race is specifically geared towards thievery, as is the Rogue personality.

##### Mage

Similarly to the Thief style above, magic-only players are normally called "pure" mage or "supermage". Likewise, they do not attack, nor do they carry out thief operations beyond simple intel gathering, instead relying on spells like Fireball, Tornado and Meteor Shower. Elves and Faeries make excellent mages, and the Mystic personality is a vital and natural choice for the pure mage.

##### Warning

It is worth mentioning that both the supermage and superthief are generally considered to be poor choices. While their respective talents are often unmatched, many players and kingdoms believe that to focus on only one discipline of the three is, for lack of a better word; lazy. While attempting to play all three styles is generally not recommended unless the player is very confident in his or her abilities (though confidence alone isn't enough), simply playing one style is often inefficient though it *can* be done with quite startling effects if the player is experienced enough. As an example, even as traditionally "pure" a thief race as Halfling has qualities that makes it a worthwhile choice for attacking. Pure attacker is not generally seen as a problem, but it is often possible to dabble in the arcane or the underground while retaining an impressive army.

#### Hybrid

As explained above, any player who uses only one discipline (attacking, thievery or spellcasting) is known as a pure member of that discipline. Conversely, any player who uses two or more disciplines is known as a hybrid. Hybrids are normally differentiated by a slash (/) between the two chosen disciplines, and are often referred to ingame by the first letter of each style. For example, an Attacker/Thief is known as an A/T.  If the attacker/thief is more geared towards thievery, they would be designated a/T, a strong magic user who also uses thievery on the side would be t/M.
The possible variations are:

##### Attacker/Thief

As expected, attacker/thieves both hit for land and use their thieves to steal, kidnap or kill enemy resources, peasants and troops (respectively). Halflings and Humans make excellent attacker/thieves, whereas Dwarves make poor ones, and virtually any personality bar Mystic comes recommended. Rogue, once again, is especially useful.

##### Attacker/Mage

Using both armies and magic, attacker/mages are often deployed against an enemy's economy as well as their lands. Elves make excellent A/Ms. Mystic isn't a requirement to be a useful A/M, but without it many struggle to build up the necessary number of wizards to be an effective mage and therefore need more time to get ready.

##### Thief/Mage

Thief/Mages (T/M) rather obviously utilize both thief operations and spells. They seldom send out troops (often not having any useful offense whatsoever), instead focusing on crippling enemy provinces with spells. Normally this is done through extensive Nightstrikes, Meteor Showers, Fireballs and other assaults from several players onto one enemy province. Once their target has been sufficiently softened up, the attackers move in to take the acres. Halflings and Faeries make strong T/Ms.

##### Attacker/Thief/Mage

Seldom seen, the A/T/M is a challenging effort to play all three disciplines at once (most who attempt it fail... most being more than 99%). Due to space and income limitations it's currently extremely difficult to play as an A/T/M, but it can be done. At the players own risk. The writer is nowhere near skilled enough to guess what the "best" choice for this playing style is. If you're new to Utopia, it's highly recommended you **don't** try to play as this.

#### Explorer/Bank

Normally only attempted by top kingdoms, a bank is an extremely large province that from early in the age is made to grow to tremendous size with the aid of the rest of the kingdom. He or she then performs many useful tasks, such as paying for and killing dragons and aiding the growth of the smaller provinces in the kingdom. Humans make excellent banks, as do Dwarves, usefully combined with the Sage or Merchant personalities.
An explorer is related but different. While banks are a kingdom-wide effort, explorers normally involve one player growing exclusively for his/her own benefit, often to the detriment of their kingdom-mates. Explorers are generally regarded as "useless" as they do not attack, perform ops or cast spells. Explorers are considered selfish and undesirable by most kingdoms. Dwarves are excellent explorers, but any race can do it, as can any personality.

## Honor

**Honor** is a measure of a player's playstyle. Honor is earned by doing "noble" deeds such as competing against players your own size and working with your kingdom.
Achieving Honor Points is a process - you gain honor by taking risks and capturing it. As you begin your fledgling province in Utopia, you will gain some honor just for surviving in the harsh world around you. After this initial period, Honor can be gained through successful attacks, spells, and thievery operations. It is important to understand, however, that notoriety only comes by taking risks - and succeeding. You will not gain honor for taking advantage of smaller, weaker enemies, or by being a pest towards substantially larger opponents.
As Honor can be gained, it can also be lost. Because Honor is captured and not created, if you are defeated by a worthy adversary, not only will he or she gain Honor, but you will lose it. Anonymity does not destroy honor during war and the attacker will not gain honor at any time when uses anonymity.

### Contents

- 1 Titles of Nobility

1.1 Honor when province is created
1.2 Honor Effects

1.2.1 Bonuses from Knight/Lady to Viscount/Viscountess
1.2.2 Bonuses from Count/Countess

1.3 Honor & Vacation Mode

Titles of Nobility

Honor Ranks | Effects
--- | ---
♂         Rank         ♀ | Lower Range | Upper Limit | Population | Offensive Military Efficiency | Income | Food | Runes | Mod WPA | Mod TPA | Votes
Peasant    Knight Lord Baron Viscount Count Marquis Duke Prince    / / / / / / / /    Lady Noble Lady Baroness Viscountess Countess Marchioness Duchess Princess | Peasant | Knight Lord Baron Viscount Count Marquis Duke Prince | / / / / / / / / | Lady Noble Lady Baroness Viscountess Countess Marchioness Duchess Princess | 0 751 1501 2251 3001 3751 4501 5251  6001 | 750 1500 2250 3000 3750 4500 5250 6000  ∞ | 1 1.01 1.02 1.03 1.04 1.06 1.08 1.1  1.12 | 1 1.01 1.02 1.03 1.04 1.06 1.08 1.1  1.12 | 1 1.02 1.04 1.06 1.08 1.12 1.16 1.2  1.24 | 1 1.02 1.04 1.06 1.08 1.12 1.16 1.2  1.24 | 1 1.02 1.04 1.06 1.08 1.12 1.16 1.2  1.24 | 1 1.03 1.06 1.09 1.12 1.18 1.24 1.3  1.36 | 1 1.03 1.06 1.09 1.12 1.18 1.24 1.3  1.36 | 1  2  3  4  5 7 9 10   10
Peasant
Knight Lord Baron Viscount Count Marquis Duke Prince | / / / / / / / / | Lady Noble Lady Baroness Viscountess Countess Marchioness Duchess Princess

### Honor when province is created

If a Province is created when the age begins, the Honor value is initialized to 0. Additionally, over a period of 3 days, Honor is raised 20 points per Tick, resulting in a total of 1440 Honor points added.

### Honor Effects

**Effects of Honor =** Above Effect from table * Race Modifier * Personality Modifier

#### Bonuses from Knight/Lady to Viscount/Viscountess

Bonuses are initially awarded upon receiving the title Knight or Lady. For titles after Knight or Lady the following bonuses are added upon any previously awarded bonuses until Count/Countess at which point the bonuses change:

1% Increase in your maximum population
1% Increase in your offensive military efficiency
2% Increase in your income
2% Increase in your food production
2% Increase in your rune production
3% Increase in your magic effectiveness
3% Increase in your thievery effectiveness
One additional vote for your Kingdom's Monarchy
 ****Note: these bonuses are modified by Race and Personality modifiers.***

#### Bonuses from Count/Countess

Upon receiving the title Count or Countess the following bonuses are added to any previously awarded bonuses until Prince, the highest title available:

2% Increase in your maximum population
2% Increase in your offensive military efficiency
4% Increase in your income
4% Increase in food production
4% Increase in rune production
6% Increase in your magic effectiveness
6% Increase in your thievery effectiveness
One additional vote for your Kingdom's Monarchy
 ****Note: these bonuses are modified by Race and Personality modifiers.***

### Honor & Vacation Mode

If you enter vacation mode within the first days of the game you will not gain honor while in vacation mode. In addition, once you exit vacation mode your honor will not receive hourly increases unless it is still within the first days of the age. This can leave your province far below the normal for honor points.

## Island

The world is divided into islands with an ocean. As the age progresses, more islands will become available to view using the Kingdom view page.
The last island and first one are neighbors. On the World of Legends server, there are currently 20 islands.
World of Legends Islands for the Current Age are:

Number | Name
--- | ---
1 | Astel
2 | Corsov
3 | Escania
4 | Farlov
5 | Harkolia
6 | Islia
7 | Jarn
8 | Kamoria
9 | Linst
10 | Mortov
11 | Nen
12 | Porsta
13 | Rastov
14 | Targo
15 | Verdok
16 | Xanth
17 | Zark
18 | Cantora
19 | Icia
20 | Narsta

Island names used in previous ages are:

- Alia

- Arcadia

- Barkonia

- Britannia

- Darth

- Dorf

- Enia

- Fort

- Gaia

- Gardonia

- Harton

- Justa

- Kangoon

- Lionia

- Maui

- Olav

- Orb Island

- Plon

- Quanti

- Rogu

- Serpent Isle

- Spinia

- Tartov

- Ugena

- Utosia

- Vienna

- Wallace

- Worz

- Yalto

- Yie

## Kingdoms

CONTENTS: Kingdoms | CONTENTS: Kingdoms
--- | ---
CONTENTS: Kingdoms

This is a contents page for the category **Kingdoms**. When you are creating a new Article/Page for a kingdom, use the following code:
{{kingdom}}
{{Infobox_Kingdom
|alliance=
|founder=
|leaders=
|website=
|contact=
|age founded=
|footnotes=
}}

### Pages in category "Kingdoms"

The following 14 pages are in this category, out of 14 total.

#### K

- Template:Kingdom

- Kingdom

- Kingdom:Bring It On

- Kingdom:Copy Cats

- Kingdom:Elitist Jerks

- Kingdom:Free

- Kingdom:Pulse

- Kingdom:Rapture

- Kingdom:Sanctuary

- Kingdom:Secrets

- Kingdom:Silly Pink Ghetto Cats

- Kingdom:Warcry

- Kingdom:Warsong

- Kingdom:Zenobia's Zealots

## Land Whorring Tips & Tricks

This is part of the Utopia WIKI Player written guides.
---

THIS PAGE is a guide aimed to cover Land Whorring Tips & Tricks. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page. | THIS PAGE is a guide aimed to cover Land Whorring Tips & Tricks. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.
--- | ---
THIS PAGE is a guide aimed to cover Land Whorring Tips & Tricks. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.

### Contents

- 1 Keep your Networth Low

1.1 Why?
1.2 Tips

- 2 Hit Smart

2.1 Why?
2.2 Tips

### Keep your Networth Low

#### Why?

- Makes it easier to find targets

#### Tips

- Put your army in training - you get rid of soldiers + gc, hence your NW drops

- Don't build till after you attack

- Army in, Army out - your peasantry wouldn't have filled therefore your NW is lower.

### Hit Smart

#### Why?

- So you don't get retaled.

#### Tips

- Look for over-defended explorers that are unable to retal, especially lone provinces / TMs.

- Always scout every potential threat in the kingdom you plan to attack in. No one wants to suffer a retal for your hit.

## Leadership Logic

**Presented by Warbirds.**
Written By W1nd. Taken from the forums on 12-12-2020: http://forums.utopia-game.com/showthread.php?640070-Warbirds-Presents-Leadership-Logic

### What about these 10 laws of effective leadership and 6 eternal principles of the constitution I hear about?

Well, I will start with the nuts and bolts, because I really enjoy talking about our kingdom's constitutional structure. Our kingdom has functioned as an elective monarchy since the end of our second age. At the end of every age our kingdom votes on goals and direction for the next age. Things like level of competitiveness and level of activity expected from players, criteria for recruitment, age goal, kd name, and theme for the age are decided by straw polls and secret ballot.
Once our age goals are decided upon, we hold a formal election to select a monarch for the next age. The only stipulation is that whoever is elected must accept the goals and direction that the kd chose for the coming age, and cannot try to change them or the constitutional nature of the kingdom. A Returning Officer is selected from the pool of original kd members, and they are entrusted with handling the nomination and selection process and ensuring a fair result of the vote.
Once a monarch is elected, the constitution stipulates that they must appoint a war leader to lead the kingdom, and a council of advisors to support the war leader. Once the war leader is appointed, the show is theirs to run however they deem appropriate. The monarch can change war leaders mid-age if they want, but not during a war in progress, and the monarch has no power to overrule or interfere with a war leader's conduct of a war.
The elected monarch has final say on withdrawing from war, recruitment, and removing players, or selecting people for leadership, but it is the war leader who is at the top of the org chart for most in-game decisions. So in some sense you could say that the kingdom runs on a consular system with two leaders; one civilian, and one military. In that sense the constitution is a formal description of the system that Smiles and I designed for ourselves out of necessity that first age. It worked well, so we made it official.
In practice, our core leadership has not changed much in 5 ages. Smiles and I have served as war leader and monarch respectively every age since our kingdom's foundation, though we do rotate people through council as often as we can to give people experience of war planning and wave leading. In the last three ages we have brought in some tremendously experienced and capable people from other kingdoms, and this expanded leadership capacity has added tremendously to our success. It also gives me great hope for the future of our constitutional experiment.
**As for RedBird's ten laws of leadership, well, these are just the rules I expect my leadership team to lead and play by:**
1. No topic of discussion is off limits in leadership council, and everyone has an equal voice there.
2. Morale is everything, and no negativity, complaining, or defeatist talk is permitted outside of council.
3. We reward initiative and encourage risk taking.
4. Everyone deserves a second chance. Most people deserve a third chance. Some people deserve a fourth chance.
5. We review personnel after every war and we are always looking for ways to make our kingdom stronger, and support players who are struggling.
6. We offer praise for positive actions, and gentle correction for mistakes. We always address the members of our kd using terms of affection and respect.
7. We always put the needs of the KD ahead of our own provinces.
8. We are decisive in giving orders and we do not argue or plead.
9. Life is more important than utopia.
10. Don't be a martyr: set a sitter and get some sleep.
**Thank you Redbird and Thank you Warbirds for being part of the community! You have a very unique kingdom structure and a nice piece of history for anyone who many have missed the early 80’s. It also serves as a very inspirational story on building a kingdom from the ground up and how you overcame struggles you faced in order to maintain a presence in the war charts age over age.**
**I would like to thank Smiles for constantly commenting and participating in the MUGA chat especially when I mention him as he has been very transparent about sharing information and data. Thank you Smiles for your contribution!**

## Magic Formulas

### Contents

- 1 Calculating Percent Guilds

- 2 Effects of Percent Guilds

2.1 Spell Duration
2.2 Self Spells
2.3 Offensive Spells

- 3 Wizards Per Acre

3.1 Raw WPA
3.2 Calculating Mod WPA

- 4 Effects of Mod WPA

4.1 Offensive Spells
4.2 Self Spells

- 5 Limit Wizard Training

- 6 Runes Cost Formula

- 7 Spell Table [Self Spells]

- 8 Spell Table [Offensive Spells]

- 9 Spells and Ability to Cast

### Calculating Percent Guilds

Unlike all your other units, either the military footmen or the thieves, wizards are not trained by using gold. Your ascendant wizards will have to go through intensive studies in Guilds before being able to serve you properly. They are an absolute necessity for Mages.
Trains 0.02 Wizards Daily (2% chance to train a Wizard per Guild)
Unaffected by BE (Building Efficiency)
Guilds also increase the duration of your self spells and offensive spells.
Guilds are unaffected by Building Efficiency for the purposes of calculating spell duration or wizards trained.
Percent Guilds, or % Guilds, refers to the current percentage of guilds a province has.

**% Guilds =** Total Number of Guilds / Total Acres

### Effects of Percent Guilds

#### Spell Duration

Percent Guilds determines Spell Duration. The higher the percent Guilds, the longer a spell will last. This remains true until the maximum Duration for that particular Spell is reached. Maximum durations can be attained when 20% of your Land dedicated to Guilds (unaffected by Building Efficiency).
Some Races or Personalities may have a bonus or penalty to Spell Duration. Destabilize Guilds lowers Spell Duration.

#### Self Spells

For Self Spells, a higher percent Guilds results in a greater:

- Spell Duration

- Chance of a Successful Cast

#### Offensive Spells

For Offensive Spells, a higher percent Guilds results in a greater:

- Spell Duration

### Wizards Per Acre

The ratio of your WPA to your opponent's WPA will determine the success rate of your conducted magic spells.

#### Raw WPA

**Raw WPA =** Number of Wizards /Acres

#### Calculating Mod WPA

Magic Effectiveness increases the WPA without changing the number of Wizards. This is known as mod WPA.

**Offensive Modified WPA =** Raw WPA * Channeling Science * Race Mod * Honor Mod * Mage's Fury Mod * Dragon Mod

**Defensive Modified WPA =** Raw WPA * Channeling Science * Race Mod * Honor Mod * Mage's Fury Mod * Magic Shield Mod * Dragon Mod

Modifier Type | Active | Otherwise
--- | --- | ---
Race: Dark Elf | 1.1 | 1
Race: Elf | 1.25 | 1
Race: Human | 0.7 | 1
Mage's Fury: Mage's Fury | 1.25 (off) / 0.75 (def) | 1 / 1
Magic Shield: Magic Shield | 1.2 (def) | 1
Ritual: Havoc | 1.25 (off) | 1
Dragon: Sapphire | 0.7 | 1

### Effects of Mod WPA

#### Offensive Spells

**Modifier =** Your Mod WPA / Opponent's Mod WPA

The higher this modifier is, the greater the:

- Chance of a Successful Cast

- Chance of Preventing an Opponent's Spell

#### Self Spells

WPA does not influence self spells.

### Limit Wizard Training

Guilds train Wizards if it allowed and current number of Wizards is less then Maximum Allowed

**Maximum Wizards Allowed to Train** = Peasants * 2

### Runes Cost Formula

**Runes cost =** *ROUNDDOWN* ( (0.6 * Size + 200) * Spell Cost Multiplier * 1.5 )

### Spell Table [Self Spells]

Spell | Description | Spell Bonus | Difficulty | Cost Multiplier | Duration (Average) | Support Spell | Av | DE | Dry | Dw | Elf | Fa | Ha | Hu | Or | Art | Cle | Her | Mys | Rog | Shep | Tact | WH | Warr
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
Minor Protection | Increases Defensive Military Efficiency by 5% (multiplicative). Stacks with Greater Protection. | 105% | 0.017 | 0.35 | 12 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Greater Protection | Increases Defensive Military Efficiency by 5%. Stacks (multiplicative) with Minor Protection. | 105% | 0.019 | 0.45 | 24 | Yes | Yes | No | No | No | No | Yes | No | Yes | No | No | No | No | No | No | No | No | No | No
Magic Shield | Increases Defensive Magic Effectiveness by 20%. | 120% | 0.022 | 0.5 | 14 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Mystic Aura | Makes the next spell cast on you fail automatically. |  | 0.022 | 0.5 | N/A | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No
Fertile Lands | Increases Food production by 25% | 125% | 0.022 | 0.5 | 16 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Nature's Blessing | Grants immunity to Storms and Droughts. Has a 33% chance to cure the Plague on a successful cast. | 100% | 0.023 | 0.6 | 16 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Love & Peace | Increases Birth Rate by +0.85% and War Horse production rate by 40%. | +0.85% | 0.024 | 0.7 | 14 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Divine Shield | Decreases Instant Spell Damage taken by 20%. | 80% | 0.024 | 0.8 | 12 | Yes | No | No | No | No | No | No | No | No | No | No | Yes | No | No | No | No | No | No | No
Quick Feet | Decreases Attack Time by 10%. | 90% | 0.026 | 0.8 | 2 | No | No | No | No | No | No | Yes | Yes | No | No | No | No | No | No | No | No | No | No | No
Builder's Boon | Reduces Construction Time by 25%. | 75% | 0.027 | 1 | 12 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Inspire Army | Reduces wages by 15% and decreases training time by 20%. | 85%/80% | 0.028 | 1.1 | 12 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Hero's Inspiration | Reduces Military Wages by 30% and Training Time by 30%. | 70%/70% | 0.017 | 1.1 | 14 | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No
Scientific Insights | Increases Science Efficiency by 10%. | 110% | 0.019 | 1.25 | 9 | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No
Anonymity | Hides province name in the next attack, but reveals Kingdom location. No Honor gains when active. Reduces attack gains by 15%. Grants Ambush Immunity for this attack. |  | 0.04 | 1.3 | N/A | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Illuminate Shadows | Reduces Damage taken from Thievery Operations by 20%. | 80% | 0.02 | 1.3 | 8 | Yes | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No
Salvation | Reduces All Military Casualties by 15%. | 85% | 0.02 | 1.3 | 8 | Yes | No | No | No | No | No | No | No | No | No | No | Yes | No | No | No | No | No | No | No
Wrath | Increases the Military Casualties of attacking provinces by 20%. | 120% | 0.021 | 1.35 | 8 | No | No | No | No | No | Yes | Yes | No | No | No | No | No | No | No | No | No | No | No | No
Invisibility | Increases Offensive Thievery Effectiveness (Offensive TPA) by 10%. Reduce Thieves lost during Thievery Operations by 20%. | 110%/80% | 0.032 | 1.35 | 12 | No | No | Yes | No | No | No | Yes | No | No | No | No | No | No | No | No | No | No | No | No
Clear Sight | Gives a 25% chance to catch enemy thieves. | 75% | 0.033 | 1.4 | 16 | No | No | Yes | No | No | No | Yes | No | No | No | No | No | No | No | No | No | No | No | No
Mage's Fury | Magic Effectiveness 25% higher for Offense, 25% lower for Defense. | 125%/75% | 0.033 | 1.4 | 6 | No | No | Yes | No | No | No | Yes | No | No | No | No | No | No | Yes | No | No | No | No | No
War Spoils | While the spell is active, you immediately take control of Land gained on Attacks. |  | 0.034 | 1.45 | 4 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Mind Focus | Increases Wizard production by 25%. | 125% | 0.033 | 1.475 | 12 | No | No | No | No | No | No | No | No | No | No | No | No | No | Yes | No | No | No | No | No
Fanaticism | Increases Offensive Military Efficiency by 5%. Decreases Defensive Military Efficiency by 5%. | 105%/95% | 0.034 | 1.5 | 6 | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Guile | Increases Instant Spell Damage and Sabotage Operation Damage by 10% for the duration. | 110% | 0.039 | 1.5 | 8 | No | No | Yes | No | No | No | Yes | No | No | No | No | No | No | No | No | No | No | No | No
Revelation | Increases the Spawn Rate of new Scientists by 20% while the spell is active. | 120% | 0.035 | 1.55 | 10 | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No
Fountain of Knowledge | Increases the Science Book production by 10% while the spell is active. | 110% | 0.033 | 1.55 | 10 | No | No | No | No | No | No | Yes | No | Yes | No | No | No | No | No | No | No | No | No | No
Tree of Gold | Instantly generates 26.66% to 53.33% of daily Income. |  | 0.025 | 1.6 | N/A | No | No | No | Yes | No | No | Yes | No | No | No | No | No | No | No | No | No | No | No | No
Town Watch | Every 5 Peasants defend with 1 strength, but suffer high Casualties. |  | 0.037 | 1.6 | 10 | No | Yes | No | No | No | No | Yes | Yes | No | No | No | No | No | No | No | No | No | No | No
Aggression | Soldiers are +2/-2 strength for the duration of the spell. | +2/-2 | 0.037 | 1.625 | 12 | No | No | No | No | No | No | Yes | No | Yes | No | No | No | No | No | No | No | No | No | No
Miner's Mystique | Peasants generate an extra 0.3gc per tick. | +0.3 | 0.038 | 1.65 | 14 | No | No | No | No | Yes | No | Yes | No | No | No | No | No | No | No | No | No | No | No | No
Ghost Workers | Lowers Jobs required for maximum efficiency by 25%. | 75% | 0.038 | 1.65 | 14 | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No
Animate Dead | In your next defensive battle, 50% your Military Casualties are returned as Soldiers. | 50% | 0.038 | 1.7 | N/A | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | Yes | No
Mist | 10% lower resource losses in battle. | 90% | 0.038 | 1.7 | 4 | No | No | No | No | No | Yes | Yes | No | No | No | No | No | No | No | No | No | No | Yes | No
Reflect Magic | 20% chance to reflect Offensive Spells back upon casters. | 20% | 0.4 | 1.8 | 12 | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | Yes | No | No | No
Shadowlight | Reveals the origin Province for the next Thievery Operation on you. Makes the next Sabotage Operation targeting you fail automatically. |  | 0.042 | 1.9 | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Bloodlust | Increases Offensive Military Efficiency by 10% and Enemy Military Casualties by 15%, but suffer 15% higher Military Casualties. | 110% 115%/115% | 0.04 | 2.0 | 6 | No | No | No | No | No | No | Yes | No | No | Yes | No | No | No | No | No | No | No | No | No
Patriotism | Increases draft speed by 30%. Lowers Propaganda Damage taken by 30%. | 130%/70% | 0.045 | 2.0 | 12 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Paradise | Creates a few acres of land. Consumes explore pool. Not available during War or Protection. |  | 0.5 | 3.0 | N/A | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Cast Ritual | Increases progress towards the chosen ritual for each cast. Only available on the Ritual tab. |  | N/A | 6.0 | N/A | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Spell | Description | Spell Bonus | Difficulty | Cost Multiplier | Duration (Average) | Support Spell | Av | DE | Dry | Dw | Elf | Fa | Ha | Hu | Or | Art | Cle | Her | Mys | Rog | Shep | Tact | WH | Warr

### Spell Table [Offensive Spells]

Spell | Description | Spell Bonus | Difficulty | Cost Multiplier | Duration (Average) | Av | DE | Dry | Dw | Elf | Fa | Ha | Hu | Or | Art | Cle | Her | Mys | Rog | Shep | Tact | WH | Warr
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
Crystal Ball | Reveals target's Throne, displaying Troops and Resources. Fully accurate. Costs 1 Mana. |  | 0.004 | 0.35 | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Storms | Kills Peasants equal to 1.5% of total Population. Cancels Drought. Increases Tornado damage taken by 15%. |  | 0.009 | 0.8 | 12 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Drought | Food production reduced by 25%. Draft Speed reduced by 15%. Kills some War Horses. Cancels Storms. Increases Arson damage taken by 15%. | 75% / 85% | 0.01 | 1.0 | 12 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Magic Ward | Unfriendly + Hostile + War: Increases the Rune Costs of target province by 100%. | 200% | 0.02 | 1.15 | 6 | No | No | No | No | No | No | No | No | No | No | No | No | Yes | No | No | No | No | No
Gluttony | Increases Food required by 25%. | 125% | 0.014 | 1.2 | 12 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Vermin | Destroys on average about 50% of target's Food. | 50% | 0.014 | 1.275 | N/A | No | No | No | No | No | Yes | Yes | No | No | No | No | No | No | No | No | No | No | No
Greed | Increases Military Wages and Draft Costs of target province by 25%. | 125% | 0.016 | 1.3 | 12 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Expose Thieves | Unfriendly + Hostile + War: Reduces target province's Stealth by 5% of current Stealth level every Tick. | 0.95 | 0.024 | 1.4 | 6 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Chastity | Reduces Birth Rate by 50%. | 50% | 0.024 | 1.4 | 6 | No | No | No | No | Yes | Yes | No | No | No | No | No | No | Yes | No | No | No | No | No
Sloth | Unfriendly + Hostile + War: Reduces Drafting Rate of target province by 50%. Increases Draft Cost by 100%. | 50% / 200% | 0.024 | 1.4 | 6 | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No
Fireball | Unfriendly + Hostile + War: Kills ~6% of opponent's Peasants. | 94% | 0.02 | 1.5 | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Fool's Gold | Unfriendly + Hostile + War: Destroys up to 25% of target's Gold. | 75% | 0.02 | 1.5 | N/A | No | No | No | No | No | No | No | No | No | No | No | Yes | No | No | No | No | No | No
Lightning Strike | Unfriendly + Hostile + War: Destroys up to 65% of opponent's Runes. |  | 0.02 | 1.55 | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Explosions | When sending aid if either the donor or the receiver are under the explosions spell, there is a 50% chance that the shipment will be reduced to 55%-80% of what it would have been otherwise. |  | 0.02 | 1.8 | 12 | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Blizzard | Reduces the building effectiveness of target province by 10%. | 90% | 0.02 | 1.8 | 6 | No | Yes | No | No | No | Yes | No | No | No | No | No | No | No | No | No | No | No | No
Pitfalls | Causes opponent to suffer 15% higher Defensive Military Casualties. | 115% | 0.024 | 1.8 | 12 | No | No | No | No | Yes | Yes | No | No | No | No | No | No | No | No | No | No | No | No
Nightmares | Unfriendly + Hostile + War: Roughly 1.5% of target's Troops are put back in Training over 8 Ticks. | 98.5% | 0.039 | 2.2 | N/A | No | No | No | No | No | No | No | No | No | No | No | Yes | No | No | No | No | No | No
Tornadoes | Unfriendly + Hostile + War: Destroys several of your opponent's Buildings. |  | 0.03 | 2.5 | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Mystic Vortex | Unfriendly + Hostile + War: For each active spell your opponent has, there's a 50% chance it's removed. | 50% | 0.031 | 2.8 | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Amnesia | War: Temporarily removes ~5% of target's total allocated Science Books. These return over 48 ticks. | 0.95 | 0.034 | 2.8 | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Meteor Showers | Hostile + War: Kills Peasants and Troops every Tick. |  | 0.04 | 3.5 | 8 | No | No | No | No | No | No | No | No | No | No | No | No | Yes | No | No | No | No | No
Abolish Ritual | Unfriendly + Hostile + War: Reduces enemy ritual strength by 2%. Limited to 10 casts on a single enemy province; see Ritual tab for more details. | -2% | 0.032 | 2.8 | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Land Lust | Unfriendly + Hostile + War: Captures between 1 and 1.25% of opponents Acres. |  | 0.04 | 4 | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No | No | No | No | No | No | No | No | No
Spell | Description | Spell Bonus | Difficulty | Cost Multiplier | Duration (Average) | Av | DE | Dry | Dw | Elf | Fa | Ha | Hu | Or | Art | Cle | Her | Mys | Rog | Shep | Tact | WH | Warr

### Spells and Ability to Cast

For full information on all of the current Spells refer to Mystics.

## Monarchy

### Contents

- 1 Overview

- 2 Monarchy: Getting Elected

- 3 Monarchy: The Monarch's responsibilities and duties

- 4 The Steward

- 5 Inactive Provinces

#### Overview

The **King** or **Queen** of a kingdom is its official representative within the larger world. Being the **Monarch** of a kingdom is quite a responsibility, and kingdoms should work to elect an experienced and capable leader. Selecting a Monarch is a simple process of voting - it is essential that all provinces participate and make their voice heard. The quality and actions of your Monarch will impact your experience and enjoyment in Utopia, and it is important to elect someone with strong communication and diplomatic skills.
A strongly united kingdom is vital to your long-term success on Utopia. Deciding on -- and listening to -- your King or Queen is an important first step, and your vote is important. Remember that a good King or Queen is not necessarily the best or most active player in your Kingdom -- it is the one with the best diplomatic ability and the one most willing to put the kingdom's goals ahead of his or her own. Take advantage of the Public Forum to discuss the vital issues of your Kingdom's future with your fellow provinces and vote for a King or Queen to lead your kingdom to glory.
The politics page allows you to vote for a King or Queen, and displays the following:

- The kingdom's current Monarch

- Minimum Votes Needed to be Elected

- Political Standings of your kingdom, i.e who has voted and how many votes they have

#### Monarchy: Getting Elected

If you wish to become the Monarch of your kingdom, there are a few different ways to achieve your goal.
First, you may be voted in by your fellow provinces. In order to be elected, you must maintain over fifty percent of the votes of other leaders, and if there are more than six provinces in the kingdom you must also clear lead of at least 2 votes than the runner up. If you are not popular, this will likely not happen. Thus, diplomacy is absolutely essential. Treat others with respect, maximize their value and importance in the kingdom. These are not only ways to earn the Monarchy, but also ideal ways to lead your kingdom to glory.
Each province in your kingdom begins with one vote. However, you can obtain additional votes and strengthen your standing through Nobility. By Utopian Law, every province is guaranteed a minimum of one vote and no more than 10 votes.
The second way to gain monarchy is to seize control of it - that is, if you have more than 50% of the total networth in the kingdom and there are at least two other provinces - your vote is all that matters. Whoever you choose to be Monarch will be elected. Unfortunately, to do this, you may have to attack your fellow kingdom provinces, weakening your kingdom's stature throughout the world. Most often, this is a strategy for failure, as you will find it difficult to lead those who do not wish to be led, but the option is yours.

#### Monarchy: The Monarch's responsibilities and duties

A Monarch must be committed to ruling with a fair hand. Seek input from your provinces, or you may quickly find yourself out of office. Each kingdom must find a Monarch to grow, but more importantly, they must find a fair and noble Monarch to lead them to glory.
It will also be your responsibility to maintain the Kingdom Council Forums, to keep them clean, and to make them a useful service to the various rulers across your kingdom. You will represent your kingdom to the world, and your actions will reflect on the provinces you represent. Diplomacy and tact will be vital to any kind of long-term successes. As Monarch, it is your duty to maintain relations with other kingdoms and organize projects such as the nurturing of a Dragon.

#### The Steward

A monarch can nominate two other players to the position of Royal Steward. These players can conduct many of the duties performed by the Monarch such as:

Changing stances
Declaring war
Conducting Ceasefires
Editing the Royal Commands
Managing the kingdom forums
Starting/Cancelling a dragon
Sending a dragon

#### Inactive Provinces

As the Monarch you have the power to destroy inactive provinces just as you could invite another leader to take over!

- Prerequisites
 First, 48 Ticks must pass from their last logoff and they will be labeled as inactive
 Second, 48 Ticks must pass for Monarch to be able to force delete/abandon of the province
 wol tick = 1 hour
 abandon will force the inactive leader out
 delete will destroy the province completely

## Multi-Attack Protection (MAP)

This is part of the Utopia WIKI Mini Guide Series.
---

THIS PAGE describes a game mechanism - Multi-Attack Protection (MAP) in utopia. It also aims to discuss the implications of this game mechanism & how others have utilized it. To discuss further implications or ask questions with regards to Multi-Attack Protection (MAP), be sure to check out the discussions page. | THIS PAGE describes a game mechanism - Multi-Attack Protection (MAP) in utopia. It also aims to discuss the implications of this game mechanism & how others have utilized it. To discuss further implications or ask questions with regards to Multi-Attack Protection (MAP), be sure to check out the discussions page.
--- | ---
THIS PAGE describes a game mechanism - Multi-Attack Protection (MAP) in utopia. It also aims to discuss the implications of this game mechanism & how others have utilized it. To discuss further implications or ask questions with regards to Multi-Attack Protection (MAP), be sure to check out the discussions page.

Multi-Attack Protection (**MAP**) (formerly known as Gangbang Protection **GBP**) is a game mechanism introduced which aims to increase the protection conferred to Provinces which have been recently hit.
Current MAP Status/Level can bee seen under Affairs of the State.
Failed Attacks also increase the MAP of the defender, based on relative Offense sent/Defense, linearly scaling from 0 to half the amount of MAP generated on a successful Traditional March.

### Contents

- 1 Effects of MAP

- 2 Attacking MAP Change

2.1 Land Attacks
2.2 Non-Land Attacks

- 3 MAP Decay

- 4 Military Effectiveness

### Effects of MAP

- The more MAP on your Province, the less an Attack will gain from you - all other variables being equal.

- Increases Military Efficiency.

- Reduced Military Casualties equal to Gains reduction

- MAP rounds off to the nearest percentage (eg. it can be 20% or 21% but not 20.5%)

- MAP is almost negligible in War.

MAP Status (Level) | MAP rating | Gains Out of War | Gains in War | Increase in ME | MAP Decay
--- | --- | --- | --- | --- | ---
Not Hit | 0% | 100% | 100% | N/A | 0
Couple | 1-20% | 80-99% | 80-99% | +0.13-2.67% | 1
Moderately Hit | 21-40% | 60-79% | 80% | +2.80-5.33% | 1
Heavily Hit | 41-60% | 40-59% | 80% | +5.47-8.00% | 2
Extremely Heavily Hit | 61-90% | 10-39% | 80% | +8.13-12.00% | 3 or 4 if above 79%

### Attacking MAP Change

#### Land Attacks

 A land attack (Traditional March, Raze or Conquest) increases the MAP rating by 2.75 * Percent of Targets land taken.

For example if a target is attacked for 120 of its 1000 acres (12%) its MAP/GBP rating will increase by(12% * 2.75 = 33%) 33 points, taking it from 0% to 33% if previously un hit - enough to put it into the 'moderately hit' section.

#### Non-Land Attacks

 Non-Land Attacks (Plunder  or Massacre) increase the MAP/GBP rating by 0.06 * Current Gains OOW
 Learn increases the MAP/GBP rating by 0.12 * Current Gains OOW

For example if a target with a MAP rating of 20% (and thus Gains OOW of 80%) which is hit for a Plunder, it will boost its GBP by (0.06 * 80% = 4.8% rounded off) 5% to 25%.

### MAP Decay

- MAP rating naturally decreases every Tick by an amount dependent on the current MAP rating as shown in the above table. For example if the MAP rating is currently 59% (heavily hit), on the next hour change it will decrease by 2% to 57%.

- MAP also decays whenever the province with MAP makes an attack.

### Military Effectiveness

 MAP gives a bonus to Military Effectiveness equal to the MAP rating / 7.5

For example if the MAP rating of a province is 59% (heavily hit) their ME is boosted by (59 / 7.5 = 7.9%) 7.9% - ie. 1.079 times it's current rating.

## Networth

**Networth** is a nominal value in gold coins of a Province/Kingdom.

Formula
**Total Networth = ** (Peasants * 0.25) + (Soldiers * Soldier NW) + (Off Specs * Offspec NW)
     + (Def Specs * Defspec NW) + (Elites * Elite NW) + (Money / 1000) + (Horses * Off value * 0.3) + (Prisoners * Off value * 0.2)
     + (Thieves * 5) + (Wizards * 7) + (Books * 0.000006 * Acres) + (Barren Land * 40)
     + (Buildings * 60) + (Buildings in Progress * 50)

Table indexes

Item | NW Value
--- | ---
Building (complete) | 60
Building (under construction) | 50
Barren Acre | 40

Item | NW Value
--- | ---
Peasant | 0.25
Soldier | (Off Points + Def Points) * 0.25
Soldier (in training) | 0
Offense specialist | Offense Points * 0.4
Defense specialist | Defense Points * 0.5
Elite | Variable (see Race entry)

Item | NW Value
--- | ---
Horse | Offense Points * 0.3
Prisoner | Offense Points * 0.2
Thief | 5
Wizard | 7
Gold | 1/1000
Food | 0
Runes | 0
Science Book | Acres * 0.000006

## Offensive Military Efficiency

### Contents

- 1 Military Efficiency

1.1 Base Military Efficiency
1.2 Offensive Military Efficiency
1.3 Defensive Military Efficiency

- 2 Attacking

2.1 Raw Offense
2.2 Modified Offense
2.3 Attack Times

2.3.1 Base Attack Time
2.3.2 Minimum Offense to Win

- 3 Attack Gains

3.1 Province Networth Factor
3.2 Kingdom Networth Factor
3.3 Attack Time Adjustment Factor
3.4 Attack Type

3.4.1 Traditional March
3.4.2 Ambush
3.4.3 Plunder
3.4.4 Learn
3.4.5 Raze
3.4.6 Conquest
3.4.7 Massacre

- 4 Defending

4.1 Minimum Defense

- 5 Military Casualties

### Military Efficiency

#### Base Military Efficiency

**Base Military Efficiency =** ( 33 + 67 * ( Effective Wage Rate / 100 ) 0.25 ) * Ruby Dragon * Multi-Attack Protection Bonus

- Rounded to one decimal point, it should return the most accurate values. Effective Wage Rate lies between 20% (77.8% Efficiency) to 200% (112.7% Efficiency).

- While wages can be changed instantly, the effective wage rate used for base military efficiency changes slowly per tick. It takes approximately 96hrs to go from 20% wages to max at 200% wages.

- Effective Wage Rate Formula = (Final Wage Rate - Previous Wage Rate)* 0.05 - Previous Wage Rate

- 96 Hour Wage Rate Chart: ME Chart

**Change in Effective Wage Rate = ** 0.05 * (Wage Rate Paid - Effective Wage Rate)

- If wages were not fully paid in the previous tick, Wage Rate Paid will be set at minimum regardless of the amount of wages actually paid.

#### Offensive Military Efficiency

**OME =** (Base Military Efficiency + Training Grounds Bonus + Honor Bonus) * Science Bonus * Race Bonus * Personality Bonus * Fanaticism * Bloodlust * Ritual

#### Defensive Military Efficiency

**DME =** (Base Military Efficiency + Forts Bonus + Honor Bonus) * Science Bonus * Race Bonus * Personality Bonus * Minor Protection * Greater Protection * Fanaticism * Plague * Ritual

### Attacking

#### Raw Offense

**Raw Off =** (Soldiers * (Soldier Off value + Aggression)) + (Offensive Specs * Off Spec Attack value) + (Elites * Elite Attack value) + (Horses * War Horse Attack value) + [(Mercs * Attack Value + Prisoners * Attack Value)]

#### Modified Offense

**Mod Off =** Raw Offense * (OME + General Bonus)

Condition | Modifier
--- | ---
OME | check your Military Advisor
General Bonus | +5% per additional general over 1

#### Attack Times

**Attack Time =** Base Attack Time * Race Bonus * Personality Bonus * Barracks Bonus * Quick Feet * Attack Type * War * NW Mod * Ritual Bonus

- Note: War Attack Speed phases in to -15%, after 12 hours of War have passed.

- There is a net worth value adjustment for attack times. This adjustment compares your net worth to the net worth of the province you are planning to attack. If these are close to each other the base attack times as given below are used. If the net worth differs, then the base attack time is multiplied, so your attack time is longer. This does not affect intra-KD attacks or in War.

##### Base Attack Time

The base attack time is 14 hours. This is the value all calculations are based upon.

Location | Intra KD | Different KD
--- | --- | ---
Attack Time | 7 | 14

##### Minimum Offense to Win

To guarantee a win, you must send Mod Offense that is at least 1 greater than the defender's Mod Defense.
On Conquest attacks, the minimum Offense to win is 51% of the opponents Defense.

### Attack Gains

For Attacks that target and capture Resources (Traditional March, Conquest, Plunder, Learn), the Gains are calculated as follows:

 **Gains** = Target Resource * Attack Type * RPNW * RKNW * Multi-Attack Protection * Race Modifier * Personality Modifier * Castles Protection * Relations Modifier * Stance Modifier * Siege Science * Emerald Dragon * Attack Time Adjustment Factor * Ritual Bonus * Anonymity * Mist

- Resources are defined as: Land, Gold Coins, Food, Runes, Science Books

- Land attacks (except Ambush) also reward Military Credits (target's Defense Points *.008 * relative NW * Military Credits mod) and Building Credits (Acres captured * 0.4 * relative NW * Building Credits mod).

- Raze ignores all modifiers except Relations, Multi-Attack Protection and the Attack Time Adjustment Factor.

- Massacre ignores most Resource Gains modifiers, except RPNW, RKNW, Relations, Multi-Attack Protection and the Attack Time Adjustment Factor; Massacre is affected by Massacre Damage mod.

- Ambush ignores all modifiers except increased/decreased Ambush Battle Losses mod.

#### Province Networth Factor

 **Relative Province Networth **(rpnw) = Targets Networth / Self Networth

 **Province Networth Factor =** *DEPEND* ( rpnw ) :
                                     rpnw < 0.567   = 0
                             0.567 < rpnw < 0.9     = 3 * rpnw - 1.7
                             0.9   < rpnw < 1.1     = 1
                             1.1   < rpnw < 1.6     = -2 * rpnw + 3.2
                                     rpnw > 1.6     = 0

#### Kingdom Networth Factor

 **Relative Kingdom Networth **(rknw) = Target Kingdom Average Prov. Networth / Self Kingdom Average Prov. Networth

 **Kingdom Networth Factor =** *DEPEND* ( rknw ) :
                                    rknw < 0.5      = 0.8
                              0.5 < rknw < 0.9      = rknw / 2 + 0.55
                                    rknw > 0.9      = 1

**NOTE**: RKNW is based on the Average Province size of the Kingdom.

#### Attack Time Adjustment Factor

Adding or subtracting hours modifies the Gains (based on your Attack Time), as follows:

Hours | Gains Modifier %
--- | ---
-2 | (-2 / base attack time) * 160%
-1 | (-1 / base attack time) * 150%
+1 | (1 / base attack time) * 80%
+2 | (2 / base attack time) * 70%
+3 | (3 / base attack time) * 60%
+4 | (4 / base attack time) * 50%

#### Attack Type

##### Traditional March

Base gains are 12% and are capped at 20% of your Acres or your opponent's Acres, whichever is smaller.

##### Ambush

- Will return 50% of the Acres lost in the attack.

- Unaffected by Gains modifiers.

- Inflicts 15% increased Military Casualties.

##### Plunder

- Base gains are 50% gold, 60% food and 60% runes.

- Max gains is 1.75x base (67.5% gold, 81% runes/food).

- Military Casualties on Plunder defense are reduced by 50%.

##### Learn

- Steals ~2% of target's allocated Books, plus ~2% of the target's unallocated Books.

- During War, Learn temporarily removes ~35% of total allocated Science Books, these return over 48 Ticks.

- Military Casualties on Learn defense are reduced by 50%.

##### Raze

- Destroys a portion (~5%) of the target's Land.

- In War, this attack only destroys ~30% Buildings.

##### Conquest

- Base gains are 6.8% land for a full hit, Gains are decreased in proportion to the relative Offense sent vs. target's Defense.

- Available only within 5% Net Worth range outside Hostile/War, unless attacker has access to Enhanced Conquest.

##### Massacre

Base gains are 9.5% peasants, 7.5% Thieves and 5% Wizards. Efficiency increased roughly 3x during War.

### Defending

**Raw Defense =** (Defense Specs * Def Spec Points) + (Elites at Home * Elite's Defense) + (Soldiers *  Sold Def Points * Aggression) + Townwatch

**Mod Defense =** *MAX* ( Raw Defense * Defensive Military Efficiency , Land )

Modifier Type | Active | Otherwise
--- | --- | ---
Def Spec Points | Variable | 10
Elite Defense | Variable
Town Watch | Peasants / 5 | 0

#### Minimum Defense

- All land is protected by a minimum of 1 defense per Acre.

- Opponent needs one offense to break your defense

- This does not apply to Intra-Kingdom attacks.

### Military Casualties

Base Military Casualties are 6.5%-8.5% on Offense, 5%-6.5% on Defense.

Modifier | Type | Effect
--- | --- | ---
Building: Hospitals | All Military Casualties | Varies
Science: Resilience | All Military Casualties | Varies
Multi-Attack Protection | All Military Casualties | Varies
Attack: Learn | Defensive Military Casualties | -50%
Attack: Plunder | Defensive Military Casualties | -50%
Attack: Failed | Defensive Military Casualties | -35%
Race: Orc | All Military Casualties | +15%
Ritual: Stalwart | All Military Casualties | -20%
Ritual: Onslaught | Offensive Military Casualties inflicted | +15%
Spell: Pitfalls | Defensive Military Casualties | +20%
Spell: Bloodlust | Offensive Military Casualties inflicted, Self Military Casualties | +15%
Spell: Salvation | All Military Casualties | -15%
Spell: Wrath | Enemy Military Casualties | +20%
Operation: Bribe Generals | All Military Casualties | +20%
Emerald Dragon | All Military Casualties | +20%

## Overpop Mitigation

This is part of the Utopia WIKI Player written guides.
---

THIS PAGE is a guide aimed to cover Overpop Mitigation. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page. | THIS PAGE is a guide aimed to cover Overpop Mitigation. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.
--- | ---
THIS PAGE is a guide aimed to cover Overpop Mitigation. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.

### Contents

- 1 Introduction

- 2 Maintaining Army

- 3 Land Lust Farm

- 4 Fireballs From Friends

- 5 WPA in the Abyss

### Introduction

Mitigating overpop is a mechanic that really privileges activity and it is not expected in most kd?s that you do these things when being chained. If you do nothing else but mass LL before troops get home so as to be able to send out easily this is still better than nothing. However, lots of wars are won or lost by how successful chains are, and these things make chains fail. One of the most significant differences between top-tier kd?s and standard war kd?s is their commitment to overpop control and maintaining a strong ?small? group of provs.
Mitigating overpop as you go down in a chain is good for lots of reasons: 1) if you have enough land coming in with armies you end up losing nothing and the chain is completely useless, 2) without losing defense you are able to maintain higher def, often preventing multi-taps which can also decrease chain success. 3) At the bottom of a chain defense is, perhaps counterintuitively, often more valuable than offense.
The basics are still the same as you do in most kd's: have lots of acres incoming, army-in army-out, release to dragon if you have to before sending out. Here are a few formulas and tricks though.

### Maintaining Army

Maintaining your army through overpop depends on one fundamental formula:
**Military desertion formula**: ((((total pop-(peasants*.1))/maxpop)-1)/5) * (soldiers + specs + elites + thieves)
Note: You only desert if maxpop*1.15 is **less than** totalpop-(peasants*.1). So if you have 10k total pop and 9k maxpop, you're not deserting.
You lose up to 10% of your peasants/tick when you are overpop, and they leave prior to desertions.
If this number is equal to the amount of soldiers you have, you only lose soldiers for the tick. This is why pers/race bonuses that return dead troops as soldiers are are so valuable when lots of people use IRC, because you use the soldier pool to prevent casualty losses. A good kd will use the soldiers generated to try to bounce provs and feed others. A great kd will use the soldiers to make it as if the prov was never chained in the first place.

### Land Lust Farm

Besides microing tickly loss this way (either by releasing thieves into soldiers to leave, being aided, etc.) another strategy to alleviate the destruction of chains is to setup Land Lust (LL) targets, either via AW or out of control growth. These target should not be targeted by attacks and will serve exclusively as LL farms for chained provs. The only spell not affected by -damage mods in race is LL damage, so regardless of what kind of attacker you are, if you are likely to be chained you should try to maintain 60 mana at all times. That's a lot of LL, and the target will always be very large, and have no wpa. When your land is about to come in, LL to where you would need to be once acres come in + are built and then go use your great new mwpa for fb.

### Fireballs From Friends

It may seem a strange concept, but if you want to save your army at the expense of your pesantry and you have KD mates with superior WPA, you can always ask them to fireball you a few times to lower your overpopulation issues.

### WPA in the Abyss

When you are chained, depending on your starting wizzies and how deep the chain is, wpa can make up a significant proportion of your max PPA. As such there is some(although heavily weighted) debate over whether you should keep the wizzies or release the wizzies.
**Pros to Keeping:**

    -If you keep the WPA, you wind up with high WPA provs capable of FBing potentially otherwise unoppable provs in the other kingdom
    -If you release the WPA, you LL less in subsequent waves.
    -WPA is hard to generate. If you release it one war you are likely to have horrible WPA in the subsequent wars.

**Cons to Keeping:**

    -If you keep the WPA, you wind up with a lot of lost potential military and your chained provs potentially fall behind
    -If you release the WPA, you can be intra-kd fireballed to release peasants, but it usually is better to release the WPA (several ticks) prior to army coming home, as you release WPA into peasants that you then need to lose to solve overpop.

�

## Overpopulation

Welcome to the Overpopulation Wiki page! If you're here, you are already deep into the mechanics of the game.
Overpopulation occurs when your Total Population exceeds your Maximum Population. Population information can be viewed in your Affairs of the State page under:

- "Total" for current total population and

- "Max Population" for the maximum amount of population your province can hold.

Overpopulation is a mechanic often used in War. During war, heavily overpopulating a province by taking away a lot of its land can trigger effects that will limit a province's effectiveness. Below are some of the effects and triggers of Overpopulation:

### Contents

- 1 Effects and Triggers for Overpopulation

1.1 Level 1: Population Exceeds Max Population (a.k.a Peasant Desertion)
1.2 Level 2: Population exceeds Max Population by 15% (a.k.a. Military Desertion)
1.3 Level 3: Population exceeds Max Population by 30% (a.k.a. Rioting)
1.4 Level 4: Population exceeds Max Population by 40% (a.k.a. Thieves on Strike)
1.5 Extra Effect: Military Population Exceeds Max Population (a.k.a Military on Strike)

Effects and Triggers for Overpopulation
Note that the below effects stack:

### Level 1: Population Exceeds Max Population (a.k.a Peasant Desertion)

When your current total population is larger than your max population, your peasants will leave and no new peasants will be born.

- Peasants leave at a rate of 10% of total peasants or the amount you are overpopulated by, whichever of the two is lower.

- The minimum number of peasants that will leave is 10.

### Level 2: Population exceeds Max Population by 15% (a.k.a. Military Desertion)

When your current total population is larger than you max population by 15%, everything in Level 1 will occur. In addition, your military shuts down, resulting in your army refusing to attack. Lastly, your troops, including thieves, will begin to desert. Troops both at home and out on an attack are affected by desertion.

- Desertions max at ~5.8% of total military population per tick (desertions do not start at 5.8%, they scale up to ~5.8% when extremely overpopulated).

- Desertions due to overpopulation will remove soldiers first, up to a maximum of 100% of the total desertions (as of Age 88).

- All troops, except soldiers (who follow a different rule), desert at approximately the same rate, regardless of whether they are at home or out on an attack. (i.e. same % of offensive specs, defensive specs, and elites will desert).

- Deserting troops are calculated one military pool at a time (offensive specs, defensive specs, elites). When you have soldiers, soldiers will replace as much of the overpopulation for a military as possible, one pool at a time, so it is possible for the deserting troop % of offensive specs, defensive specs, and elites to not be the equivalent.

- Deserting troops will fill dungeons first, if any space is available, before being completely lost.

### Level 3: Population exceeds Max Population by 30% (a.k.a. Rioting)

When your current total population is larger than you max population by 30%, everything in Level 1 & 2 will occur and in addition, your peasants will riot.

- Your income is reduced by 50%.

### Level 4: Population exceeds Max Population by 40% (a.k.a. Thieves on Strike)

When your current total population is larger than you max population by 40%, everything in Level 1, 2, & 3 will occur and in addition, your thieves will refuse to work.

- Cannot perform any Thievery Operations.

### Extra Effect: Military Population Exceeds Max Population (a.k.a Military on Strike)

When your current military population is larger than you max population, your army will refuse to attack. This mechanic is separate from the above levels.
(i.e. a province that has 10k max pop and 10.5k military will not be in desertions or have any other effect other than the military will refuse to attack, unless they are also above 15% overpop due to peasant+wizard count)

- Cannot use your army to attack.

## Paper Utopia

The Daily Paper lists various occurrences within a kingdom. These include attacks, deaths, and changes in relations with other kingdoms. Selecting Last Month lists the entries from the previous day. Below are possible Paper entries:

### Contents

- 1 Actions by your Kingdom

1.1 Attacks
1.2 Intra-Kingdom Conflict
1.3 Help
1.4 Individual Provinces

- 2 Actions Against Your Kingdom

2.1 Attacks

- 3 Dragon Entries

- 4 Relations News

4.1 War
4.2 Mutual Peace
4.3 Ceasefire

### Actions by your Kingdom

#### Attacks

Traditional March: | Province(x:yy) captured xxx acres of land from Enemy(x:yy). An Unknown Province from Kingdom(x:yy) captured xxx acres of land from Enemy(x:yy).
--- | ---
Learn: | Province(x:yy) attacked and looted XXX books from Enemy(x:yy). An Unknown Province from Kingdom(x:yy) invaded and looted XXX books from Enemy(x:yy).
Plunder: | Province(x:yy) invaded and pillaged Enemy(x:yy). An Unknown Province from Kingdom(x:yy) invaded and pillaged Enemy(x:yy).
Massacre: | Province(x:yy) killed xxx people within Enemy(x:yy). An Unknown Province from Kingdom(x:yy) killed xxx people within Enemy(x:yy).
Conquest: | Province(x:yy), captured xxx acres of land from Enemy(x:yy). An Unknown Province from Kingdom(x:yy), captured xxx acres of land from Enemy(x:yy).
Ambush: | Province(x:yy) recaptured xxx acres of land from Enemy(x:yy).
Raze: | Province(x:yy) invaded Enemy(x:yy) and razed xxx acres of land. An Unknown Province from Kingdom(x:yy) razed xxx acres of Enemy(x:yy).
Failed Attack: | Province(x:yy) attempted an invasion of Enemy(x:yy), but was repelled. An Unknown Province from Kingdom(x:yy) attempted an invasion of Enemy(x:yy), but was repelled.

#### Intra-Kingdom Conflict

Traditional March: | In local kingdom strife, Province(x:yy) invaded Enemy(x:yy) and captured xxx acres of land.
--- | ---
Raze: | In local kingdom strife Province(x:yy) invaded Enemy(x:yy) and razed xxx acres of land.
Failed Attack: | In intra-kingdom war Province(x:yy) attempted to invade Enemy(x:yy), but failed.

#### Help

Aid: | Province(x:yy) has sent an aid shipment to Province(x:yy).
--- | ---

#### Individual Provinces

Killed: | Alas, the once proud province of Province has collapsed and lies in ruins.
--- | ---
Inactivity: | Alas, the truant Ruler has lead Province into a state of neglect. Province has now collapsed and lies in ruins.
Abandoned: | As the ultimate betrayal, Ruler destroys all in the land of Province before leaving for a new kingdom.
Defected out: | Province has defected to Kingdom(x:yy)!
Defected in: | The province of Province has defected to us from Kingdom(x:yy).
Defected out (Invite): | The leader of Province has chosen to join Kingdom(x:yy). All in Province gather their possessions and depart this kingdom forever.
Defected in (Invite): | The leader of Province has wisely chosen to join us from Kingdom(x:yy).

### Actions Against Your Kingdom

#### Attacks

Traditional March: | Enemy(x:yy) invaded Province(x:yy) and captured xxx acres of land. An Unknown Province from Kingdom(x:yy) invaded Province(x:yy) and captured xxx acres of land.
--- | ---
Plunder: | Enemy(x:yy) attacked and pillaged the lands of Province(x:yy). An Unknown Province from Kingdom(x:yy) attacked and pillaged the lands of Province(x:yy).
Learn: | Province(x:yy) attacked and looted XXX books from Enemy(x:yy). An Unknown Province from Kingdom(x:yy) invaded and looted XXX books from Enemy(x:yy).
Massacre: | Enemy(x:yy) invaded Province(x:yy) and killed xxx people. An Unknown Province from Kingdom(x:yy) invaded Province(x:yy) and killed xxx people.
Conquest: | Enemy(x:yy) invaded Province(x:yy) and captured xxx acres of land. An Unknown Province from Kingdom(x:yy) invaded Province(x:yy) and captured xxx acres of land.
Ambush: | Enemy(x:yy) ambushed armies from Province(x:yy) and took xxx acres of land.
Raze: | Enemy(x:yy) razed xxx acres of Province(x:yy).
Failed Attack: | Enemy(x:yy) attempted to invade Province(x:yy). An Unknown Province from Kingdom(x:yy) attempted to invade Province(x:yy).

### Dragon Entries

Cancellation: | Our kingdom has canceled the dragon project to Enemy Kingdom(x:yy).
--- | ---
Enemy Cancellation: | Kingdom (x:yy) has cancelled their dragon project targeted at us.
Starting a Dragon: | Our kingdom has begun a (type) Dragon project, (dragon name), targeted at Kingdom(x:yy).
Enemy Kingdom Starting a Dragon: | Kingdom(x:yy) has begun a (type) Dragon project, (dragon name), against us!
Sending a Dragon: | Our dragon, (dragon name), has set flight to ravage Kingdom(x:yy)!
Receiving a Dragon: | A (type) Dragon, (dragon name), from Kingdom(x:yy) has begun ravaging our lands!
Slaying a Dragon: | Province has slain the dragon ravaging our lands!
Dragon Flies Away: | The dragon ravaging our lands has flown away...

### Relations News

#### War

Declaration: | We have declared WAR on Kingdom(x:yy)!
--- | ---
Enemy Declaration: | Kingdom(x:yy) has declared WAR with our kingdom!
Surrender: | Unable to achieve victory, our Kingdom has withdrawn from war with Kingdom(x:yy). Our failed war has finally ended!
Enemy Surrender: | Kingdom(x:yy) has withdraw from war. Our people rejoice at our victory!

#### Mutual Peace

Proposal: | We have proposed a Mutual Peace to end our war with Kingdom(x:yy)!
--- | ---
Enemy Proposal: | Kingdom(x:yy) has proposed a Mutual Peace to end our war!
Accepted: | We have accepted an offer of Peace by Kingdom(x:yy). The people celebrate the end of our War!
Enemy Accepts: | Kingdom(x:yy) has accepted our offer of Peace. The people celebrate the end of our War!

#### Ceasefire

Proposal: | We have proposed a ceasefire offer to Kingdom(x:yy).
--- | ---
Enemy Proposal: | Kingdom(x:yy) has proposed a formal ceasefire with our kingdom.
Withdrew Proposal: | We have withdrawn our ceasefire proposal to Kingdom (x:yy).
Enemy Withdrew Proposal: | Kingdom(x:yy) has withdrawn their ceasefire proposal.
Accepted: | We have entered into a formal ceasefire with Kingdom(x:yy).
Enemy Accepts: | Kingdom(x:yy) has accepted our ceasefire proposal!
Terminated: | We have canceled our ceasefire with Kingdom(x:yy)!
Enemy Terminates: | Kingdom(x:yy) has broken their ceasefire agreement with us!

## Protection

For a period of 24 hours after Freeze time ends and for the same period once you create a new account, your province is under Protection. During this time your province is unable to send Aid, change the Wage rate, cast on Rituals, fund or slay Dragons; you cannot interact with other provinces, except to receive Aid. This period is used to prepare your province for exposure to the game world. Provinces under Protection are displayed on the Kingdom Page in green text, and with a trailing ^ after their province names.
Provinces joining a Kingdom during War will be subject to a Freeze time which lasts until the end of the War. You will start with less resources.

## Province

A province is the collection of acres to which province is allotted.

### Contents

- 1 Creation

- 2 Destruction

- 3 Abandonment

- 4 War

#### Creation

Creating a province is easy and free.

#### Destruction

A province can be lost or destroyed if it's total acres drop down to 0.

#### Abandonment

A province can be abandoned but the lands kept intact for a new leader to take over or, in an act of ultimate betrayal, they can be completely destroyed.

#### War

Provinces created/reset during War will start without Soldiers, Military & Building Credits.

## Quick Tips

This is part of the Utopia WIKI Player written guides.
---

THIS PAGE is a guide aimed to cover Quick Tips. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page. | THIS PAGE is a guide aimed to cover Quick Tips. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.
--- | ---
THIS PAGE is a guide aimed to cover Quick Tips. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.

### Quick Tips

**These tips are largely targeted towards newer players, although some of these may be helpful to more veteran players as well**

**Quick Attacking Tips**

- If you are in war with ~12 hour attack times, and want your ambush armies to come home the same time as traditional march armies, add hours(normally 3).

- Limit time between getting intel and hitting, especially if they are online! Soldier aid, plague removal, casting town watch and casting protection can all bounce you if you are not quick.

- If you are being hit in war, always traditional march before you ambush. You gain gbp every time you are hit, but it rapidly decreases as you hit out. While TM?s use military efficiency(something GBP gives), ambushes do not. If you are hitting the same person with both the traditional march and the ambush, this is even more important as if they want to ambush your large TM, they will first have to go through your ambush

- If you don’t have enough offense for many taps, or to ambush multiple armies from same prov, you can send 1 troop on an ambush, and open up the bigger army to ambush from your troops

- In most instances(especially if you are a new player), if you are an attacker you should try to keep your army out at all times. It’s better to extend attack time so that you can send out when its home than to have a quick attack time that leaves troops home.

- If you aren’t attacking with all generals, use more generals on your larger attack. Generals add .03% military(additive) to the army you are sending.

- Ambushing counts as a failed attack.

- Time you may want to anon in war: you will have largest hit on a chain target. You are only tapping that chain target once(and it is a top acre grab). You have very low def elites and are hitting few taps into few provs(ambush kills elites)

- Times you probably don’t need to anon in war: you’re in the middle of a chain on someone. You use a high defensive elite/ospec. You’re multi-tapping them. Your army will get back before theirs.

- Heading into war, make sure your KD has intel, and not just SoT’s on all provs. Surveys and infiltrate thieves guilds are also important!

- Try not to start war with low def elites home(if you are a top offense prov in kd) or away with no land incoming. A chain will severely hurt you, and thus your KD.

- Dungeons do not increase enemy casualties. At max, they take half the would be casualties, and convert them into prisoners. If you are attacking(especially multi-tapping) a couple % of dungeons is verrrry effective(~2%).

**Quick Opping Tips**

- Op success is based on the ratio of tpa/wpa between opper and the target. This means in the right circumstance a prov you would normally think of as purely and attacker, can also op.

- Sapphire Dragon affects op success.

- Night Strike affects troops both home and away

- +damage mods on magic do not affect any self spells, land lust, and part of fireball

- For magic ops, relative wpa * difficulty of spell determines success rate*NW. Guild % * BE * race/pers effects duration, and success rate for self spells(20% is the maximum). A FB, LL or MV is as effective with 0% guilds as with 20%.

- Different spells are more or less effective on different provs. MS for example is much better on bigger provs; riots are much better on provs with better economies, ect. Don’t think you need every spell on every prov.

- Greed works on any prov, regardless of whether or not they are immune to econ mods.

- In current rules, the only cost reduction on thieves(besides halfer) is from eowcf.

**OOW**

- If you are not whoring, then you should only random provs that are in KD?s your KD would be willing to war. If they have offense they may hit back. If in a whoring kd, just read Godly's guide.

- If you outgrow your kd, expect to be hit. The cores of kd’s that want your land will be larger than your core.

- After war, if you are suddenly severely underpopped, watch out for starvation as the peasants may come in rapidly.

- If you are in a war kd, then learning is probably a better way of "sci pumping" than actual sci pumping.

**Misc.**

- Most kd?s do similar strategies in war. Learn these strategies and tweak your prov accordingly. If you are a top offense prov, a top econ prov, or likely to become an unbreakable prov, you may be chained and should have more GS than if, say, you are completely middle of the pack against a kd that chains.

- In most cases, don’t get too worked up over some static “build.” Outside of certain cases(and protection) your province will be dynamic, and you should react accordingly. Figure out what buildings do, and who they are best on in what situation.

- warrior bonus does not show up in throne page, SoT's, or SoM's

- In general, don’t be a jerk to kd-mates.

**Strategy Links**:

- http://forums.utopia-game.com/showth...ealest-Returns

- http://forums.utopia-game.com/showth...e-advantageous

- http://forums.utopia-game.com/showthread.php?628905-Guide-to-growing-n-stuff

## Recommended Defense

This is part of the Utopia WIKI Player written guides.
---

THIS PAGE is a guide aimed to cover Recommended Defense. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page. | THIS PAGE is a guide aimed to cover Recommended Defense. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.
--- | ---
THIS PAGE is a guide aimed to cover Recommended Defense. It comprises of tips and tricks written by other players, for regular utopians. Please be civil in your discussions if you disagree with a point made on the page.

Updated for Age 89. 2021-1-1. Special thanks to W1nd for the advice.

### Introduction

You will hear/read many varying accounts on how much defense you should run.  This is a recommendation for new players who wish to learn more about the game mechanics but don't have a teacher at hand.  This (very short) guide covers DSPA and is a basic anchor to help new players get started on how much defense they need to build.

- Defense Specialists per Acre = DSPA

### Strategy

**Proper defense alone can only help you so much. Defense needs to be combined with a certain level of deterrence. High offense for example will make enemies think twice about hitting your province.**
If you run enough defense to prevent being double tapped by people in your networth range, you will be okay.
Depending on Race and Personality choices, using these numbers as a base (tweak to fit your playstyle/strategy) will help you on your way to becoming the best.

### Basic Guideline

In most scenarios unless you are in eowcf (End of War Cease Fire), you want to be somewhere between 50-70% drafted in the military.
Here is a very simple guideline for suggested DSPA (Defense per Acre) if you need something to start with:
**In the beginning of the age for all players coming OOP (out of protection)**:

DSPA - 3 to 4
TPA (Thief per acre) - 1
OSPA (Offensive spec per acre) - Whatever else you have

At this point, you will have barely hit 50% military and most of your military units will be specialists. As an attacker, you will want to typically aim for 2:1 offense spec to defense spec.
**Attacker @ 1000acres**:

DSPA - 6 to 7
TPA - 2 to 3
OSPA/EPA (Elites per acre) - Balanced based on EOWCF income

EPA is dependent on several factors; income, war wins, cease fires, science goals, builds and overall kingdom plan for the age. Most kingdoms advocate that getting to full Elites would be best ASAP.
**TM @ 1000acres**

DSPA/EPA - MAX within funding limits
TPA - 3 to 5+

This is an initial recommendation for pure TMs. Note that you'll have to take into consideration Elite points for different races as one of the many factors to consider. For example, elves have stronger dspec (defensive specialists) than its elites on defense so they would not train elites normally, while Faeries have tough defense on their elites, so you would want to convert to elites ASAP.

## Relations

Attacking another kingdom affects the relations between the two kingdoms.
By continually attacking, your kingdom's conflict level against the opposing kingdom will elevate, thereby changing the relation type; first from **Normal** to **Unfriendly**, and then **Hostile**.
There are five relation types, each of which have various benefits and penalties.

### Contents

- 1 Relation Types

1.1 Normal
1.2 Unfriendly

1.2.1 Effects

1.3 Hostile

1.3.1 Effects
1.3.2 Summary

1.4 Ceasefire

1.4.1 Agreed Ceasefire
1.4.2 Forced Ceasefire

1.5 War

1.5.1 Immediate Effects
1.5.2 After 12 Hours
1.5.3 After 24 Hours
1.5.4 Fake War
1.5.5 Province Creation

- 2 Starting a War

- 3 Relation Table

- 4 Ending a War

4.1 Mutual Peace
4.2 Withdrawal
4.3 Victory
4.4 End-of-War Ceasefire

- 5 Out-Of-Range War Benefits

- 6 War Forum

Relation Types
Each kingdom will have differing relations amongst one another in the world of Utopia. How these relations evolve (or fall apart) will be dependent on the history, conflict level, and diplomatic abilities of the Monarchs and their Stewards. You can see your relation with any given kingdom by viewing their respective Kingdom page. It is indicated as such:

 Their Attitude Towards Us : XX
 Our Attitude Towards Them : YY

### Normal

- No effects

This is the default relation between all kingdoms from the start of the Age. **Normal** relations will resume after a **War** or **Ceasefire** ends.

### Unfriendly

*Unfriendly* is the first elevated stage of diplomatic tension between kingdoms, granting access to additional hostile actions.
When the Hostility Meter reaches **15 hostility points**, the aggressor kingdom’s stance changes to **Unfriendly** toward the target kingdom. This unlocks stronger offensive Spells and Thievery.

#### Effects

Gains | Military Casualties | WPA/TPA | Attack Time | OME
--- | --- | --- | --- | ---
+4% | –5% | +5% | –2.5% | +2%

Gains | Military Casualties | WPA/TPA | Attack Time | OME
--- | --- | --- | --- | ---
+1.5% | –2.5% | +2.5% | –1% | +1%

### Hostile

*Hostile* is the second level of diplomatic tension between kingdoms, marking a major escalation in aggression.
When the Hostile Meter reaches **30 hostility points**, the aggressor kingdom’s stance becomes **Hostile** toward the target kingdom. Dropping below this threshold returns relations to **Unfriendly**. Hostile status unlocks powerful offensive Spells and Thievery, including Meteor Showers, and reduces mana and stealth costs for hostile actions to **2%**.

#### Effects

Gains | Military Casualties | WPA/TPA | Attack Time | OME
--- | --- | --- | --- | ---
+10% | –12% | +15% | –6% | +5%

Gains | Military Casualties | WPA/TPA | Attack Time | OME
--- | --- | --- | --- | ---
+3% | –4% | +5% | –2% | +2%

#### Summary

Hostile relations represent a significant step toward open conflict, offering access to devastating hostile operations and spells. This stage is often a precursor to full-scale War.

### Ceasefire

##### Agreed Ceasefire

Also known as a **Non Aggression Pact** (as seen on the opposing kingdom page and when targeting with spells/ops).

- Prohibits any Attacks, Spells, or Ops between opposing kingdoms

- Annuls Hostility Meter

- Minimum duration of 1  Utopian Month

- Can be enforced for a max of 3 Utopian Years

Both Monarchs and Stewards can send, accept, and break Ceasefires. Once accepted, the Ceasefire agreement cannot be broken for the next 24 hours, though the Monarch or Steward can choose to extend this date no further than 3 weeks. While a Ceasefire is in effect, no hostile actions will be allowed between the two Kingdoms.

##### Forced Ceasefire

In the event that a Defending Kingdom is unable to withstand the might of an Aggressor Kingdom, they will be given the option to Surrender.
A Defending Kingdom can enter into a 96 Ticks unbreakable Ceasefire with an Aggressor Kingdom if:

- the Aggressor Kingdom has reached Hostile Relations with the Defending Kingdom

- the Defending Kingdom has not reached Hostile Relations with the Aggressor Kingdom

- the Defending Kingdom is out of War Range (85%-117.64%)

- the Defending Kingdom has not committed any Attacks within the past 3 hours (similar to the 2-hour restriction on withdrawing from War); this timer does not apply if the Defending Kingdom is at War, hostile Sorcery or Thievery Ops will not reset this timer

- the Defending has not sent any Dragons for at least 3 ticks

- the Aggressor has been Hostile towards the Defender thru at least 4 ticks (for example: Aggressor reaches Hostile on the 9th. The 10th is tick 1, 11th is tick 2, 12th is tick 3, 13th is tick 4; the Defender could Surrender on the 13th if all other conditions are met)

An Aggressor Kingdom can enter into a 96 Ticks unbreakable Ceasefire with a Defending Kingdom if:

- the Aggressor has not made military Attacks against the Defending Kingdom for at least 24 Ticks

- the Aggressor has not sent any Dragons for at least 24 Ticks

- the Aggressor is not at War (including EoWCF)

- the Defender is not at War (including EoWCF; timer starts when the Defender leaves War)

(the 24 Ticks waiting period will not begin until EoWCF concludes)

End-of-War Ceasefire has slightly different effects and conditions.

### War

War begins when a kingdom *declares War* on a Hostile kingdom **OR** if the maximum hostility level is reached by both Kingdoms.
In order to declare War, a Kingdom must:

- have received Attacks from at least three unique provinces on either side (except if Monarch/Stewards grant Hostile Operations)

- be in Range (more than 85% and less than 117.64% of its Net Worth or Land)

- be at least Unfriendly with the opposing Kingdom, AND that Kingdom must be Hostile with your Kingdom

*In instances where both kingdoms are **Hostile**, the Kingdom with fewer meter points will receive the "button" and be able to declare while. When 60 points are reached by both Kingdoms, either one can declare*
*If 180 points are reached by both Kingdoms, War automatically starts.*

Wars last a minimum of 2 Utopian Months (48 hours) after declaration.
A Kingdom can only War one other Kingdom at a time.
Honor and Land gains are higher in War than out of War.

#### Immediate Effects

- War overrides relations with all other kingdoms. Upon leaving War, Normal relations will resume. While in War, there is a decay of two hostility points per Utopian Month or 1/5th of the Meter, whichever is greater.

Benefits
- Mana & Stealth costs for offensive spells/ops reduced to 2%

- Unlocks Propaganda and Sabotage Wizards Operations

- Unlocks Amnesia and Expose Thieves Spells

Penalties
- Paradise cannot be cast (except during EoWCF)

- 600% Exploration Costs

#### After 12 Hours

Benefits
- -15% Attack Time

#### After 24 Hours

Benefits
- -80% Gains, Military Casualties and Effectiveness for Spells and Operations to and from other Kingdoms (this fades in from War start)

#### Fake War

Any informal or formal agreements made between kingdoms in regards to warring must abide by the Code of Conduct. Violations may cause the war to be deemed a Fake War. Fake Wars are subject to actions by the game operators. As the determination for a Fake War is made on a case-by-case basis by the game operators, the exact punishment may vary.
Ways a War can be faked (Please note, this is just an idea and not a comprehensive list):

- Requesting specific people be targeted by opposing Kingdom or accepting to action a request from the opposing Monarch

- Non-aggression pact during War of any duration and at any time

- Attempts to manipulate War-Win rankings using friends to initiate multiple Wars

- Agreement to trading Acres for a War Win

- "Ending" a war before minimum war duration

Punishments may include (Again, not a comprehensive list):

- Removal from the End of Age rankings for both kingdoms

- Deletion and temporary ban of players making the agreement

- Removal of war wins

- Monarchs of both Kingdoms deleted

- Removal of any gains of the Fake War from all Kingdom members (even if they were unaware of the Fake War)

#### Province Creation

Provinces created/reset during War will start without Soldiers, Military & Building Credits.

Starting a War
Once the **Hostile** relation status has been reached by one kingdom, the Monarch of the least hostile Kingdom will receive the option to Declare War as long as their own relations with that Kingdom are at a minimum of **Unfriendly**. This "War Button" appears on the Relations Page under the War tab. If both kingdoms have reached **Hostile** relations status, the kingdom with fewer points (while under 60 points) will have a "Declare War" button. When both kingdoms reach 60 points, the button will be available to both. Once the button is pressed certain effects are immediately applied; others slowly take effect, rising to their maximum potential over a 24 hour period.

Relation Table

Inter-Kingdoms' Relations
---
Ceasefire | Normal (0-14.99) | Unfriendly (15-29.99) | Hostile (30-180) | War
Prohibits any Attacks  Prohibits any Spells  Prohibits any Thievery Operations  Annul Hostile Meter  End Of War Ceasefire   Min 24 U-Days  Max 96 U-Days  +1000% birth rate (minimum 500) for the first 24 U-Days  Explore penalty reduced to 300% for provinces below Kingdom Median (including incoming explored Acres)  Combined with War Relations  Separate annul the Relations (War and CF)  All Land currently out with armies at War end returns home immediately  All Military Units currently out on Attacks against the War opponent return home immediately  Negative Spell effects and Riots removed  Dragon project is automatically canceled  Instant Population growth of 20% of your max population if you are under 50% of your max Population | No Effects | To opposing Kingdom:   Unlocks Unfriendly Spells  Unlocks Unfriendly Thievery Operations | To opposing Kingdom:   Unlocks Hostile Spells  Unlocks Hostile Thievery Operations   Mana cost for Offensive Spells reduced to 2%   Stealth cost for Offensive Ops reduced to 2% | Immediate Effects  Annul Hostility Meter with everyone  Benefits   +10% Combat Gains   Unlocks Propaganda thievery operation  Unlocks Amnesia spell  Mana costs for Offensive Spells reduced to 2%   Stealth costs for Offensive Ops reduced to 2%   Penalties   600% Exploration Costs  Paradise unavailable   After 12 Hours (12 Utopian Days) Benefits  -15% Attack Time   After 24 Hours (1 Utopian Month) Benefits   -80% Gains and Effectiveness for operations to and from other Kingdoms (this phases in from War start)

Ending a War
Only the Kingdom's Monarch (or Steward) is able to end a war. This is accomplished in one of two ways: Mutual Peace or Withdrawal. Either choice results in an end-of-war ceasefire.

#### Mutual Peace

This option requires consent by both parties and simply settles the war with no winner. This is an excellent option when both kingdoms simply lose interest in the war or find it more beneficial to simply move on.
*Both kingdoms receive:*

* 3 times your median Provinces Acres in Specialist Credits
* Free Building Credits to the total of 200% of median province total Land at the end of the War
* A provision of additional land to each province's individual Explore Pool
* Science Books bonus equal to 24 Ticks of production
* 1 additional War Score point

#### Withdrawal

Once the Minimum Time limit is reached (48 Ticks), either Kingdom can Withdraw from War. Withdrawals can occur if the Withdrawing Kingdom has not committed any Attacks within the past 2 Ticks.
War will also automatically end (a Kingdom will automatically Withdraw) if their Net Worth drops below 66% of the opponent's Net Worth on the first Tick this condition is satisfied. This will only occur after a minimum of 48 Ticks.
*The Withdrawing Kingdom receives the following **benefits**:*

* 3 times your median Provinces Acres in Specialist Credits
* Free Building Credits to the total of 200% of median Province total Land at the end of the War
* A provision of additional Land to each Province's individual Explore Pool
* Science Books bonus equal to 24 Ticks of production

*The Withdrawing Kingdom incurs the following **penalties**:*

* 5% of the Kingdom's Land will be lost and transferred to the Winning Kingdom
* 5% of the Kingdom's Honor will be lost and transferred to the Winning Kingdom

#### Victory

A Kingdom is victorious when its opponent withdraws from War. This is also called Surrendering. A Kingdom can only Withdraw if it makes no Attacks for 2 consecutive Ticks. It can then Withdraw on the 3rd Tick. Dragons, Aid, Thievery Operations and Magic Spells do not affect a Kingdom's ability to Withdraw.
*After War, the winning kingdom receives the following **benefits**:*

* 3 times your median Provinces Acres in Specialist Credits
* Free Building Credits to the total of 200% of Median Province total Land at the end of the War
* A provision of additional Land to each Province's individual Explore Pool
* Science Books bonus equal to 36 ticks of Production
* +50% advancement towards the next Scientist
* Land bonus equal to 5% of the losing Kingdom's total Land at the end of the War, subtracted from each Province then transferred and distributed evenly
* Land bonus equal to 10% of the losing Kingdom's total Land at the end of the War, distributed prioritizing smallest Provinces in the Winning Kingdom
* Honor bonus equal to 5% of the losing Kingdom's total Honor at the end of the War (subtracted from each province then transferred and distributed evenly), plus 200 Honor per Province
* Recognition on Kingdom Page based on the number of Wars achieved
* 2 additional War Score points

**Note:**

- Each additional War Win achieved will increase War Win bonuses (that are not transferred) by 5%, capped at 50% larger than baseline bonus.

- War Win bonus will incur a 5% stacking penalty for each Province below 25, calculated at War start - max 25% reduction.

- At the conclusion of the age, Kingdoms will be awarded bonus War Score points for every Kingdom that they defeated in War, based on the defeated Kingdoms' total War Wins (if any). An additional provision of points will be granted for every Kingdom warred but not defeated, based on the total War Wins of those Kingdoms (if any), a Mutual peace counts as a loss in this instance.

- War Score will incur a 4% stacking penalty for each missing Province below maximum, calculated for each individual War, this penalty carries over to EoA adjustment, full points only awarded full Kingdoms.

#### End-of-War Ceasefire

After a War ends, neither Kingdom may have any Relations for an Utopian Month and are automatically placed in a 24 hour End-of-War Ceasefire. During the ceasefire both Kingdoms remain in War relations, thus retaining the protection benefits while rebuilding. After 24 hours, the Kingdoms have the choice either to end the Ceasefire or to wait up to an additional 72 hours (96 hours total). This choice is independent of the other Kingdom.
*During this ceasefire, both sides benefit from:*

* Building Efficiency automatically restored to 100% if below 100%
* All Land currently out with armies at War end returns home immediately
* All Military Units currently out on Attacks against the War opponent return home immediately
* Negative Spell effects and Riots are removed
* Any Provinces affected by Plague it removed instantly
* Instant Population growth of 20% of maximum if you are under 50% of your maximum Population
* +1000% Birth Rate (minimum 500) for the first 24 Ticks
* Explore penalty reduced to 300% and explore time reduced by 50% for Provinces below Kingdom Median (including incoming explored Acres)
* Access to Paradise spell
* Dragons that have already begun will be automatically canceled upon entering EoWCF

**Note:**

- All Credits (Specialist or Building) will be lost upon exit of End of War Ceasefire

- Learn and Amnesia will return books over 48hrs, even if war ends.

Out-Of-Range War Benefits
There are no benefits for a War that was conducted outside of War Range (85%-117.64%). Neither winner or loser will gain Training or Building Credits and their Land and Troops will not instantly return (they will return at normal time).

War Forum
Shortly after declaring War, a temporary Forum is created. This is known as the War Forum.
In the War Forum Provinces from either Kingdom can interact by starting new threads or posting in existing ones.
Provinces are expected to interact respectfully and obey the Code of Conduct. Any offending material can be removed by either Kingdom's Monarch or Steward.

## Relations Meter

### Contents

- 1 Significance of the Hostility Meter

- 2 Attacks, Spells, Ops and How they Move the Meter

2.1 Traditional Marches, Conquests, Razes, Plunders, Massacres, Learns
2.2 Ambushes
2.3 Bounces
2.4 Dragons
2.5 Spells and Thievery Operations

- 3 Detailed: Effects of Moving the Meter & Changing Relations

3.1 Normal
3.2 Unfriendly
3.3 Hostile
3.4 War

- 4 Changelog

### Significance of the Hostility Meter

When a party hits **15 points** they become Unfriendly to the Kingdom which they hit/opped. Hostile status requires **30 points** to achieve.
If both Kingdoms reach Hostile relations, the kingdom with fewer meter points may declare war. When **60 points** are reached by both Kingdoms, either one can declare.
On the first of each Utopian Month, both hostility meters decay by **one fifth (20%) or 3 points, whichever is greater**.

### Attacks, Spells, Ops and How they Move the Meter

Different successful Attack types, Spells and Thievery Operations add to the Hostility Meter at varying levels of intensity. The Attacks add to the Meter according to the figures given below. The Meter is capped at 180 points.

#### Traditional Marches, Conquests, Razes, Plunders, Massacres, Learns

All these Attacks add 3 points to the Hostility Meter per hit.

#### Ambushes

Ambushes add 1.5 points to the Meter.

#### Bounces

- Bounces will affect the Meter based on Offense send / Defense.

- Failed Raze Attack will generate 3 meter points (Age 109)

#### Dragons

Dragons sent add 30 points to the Hostility Meter.

#### Spells and Thievery Operations

Spell | Relations Required | Value
--- | --- | ---
Storms | Normal | 0.06
Drought | Normal | 0.06
Gluttony | Normal | 0.09
Magic Ward | Unfriendly | 0.15
Chastity | Unfriendly | 0.15
Sloth | Unfriendly | 0.15
Greed | Normal | 0.15
Vermin | Normal | 0.00
Abolish Ritual | Unfriendly | 0.15
Lightning Strike | Normal | 0.18
Pitfalls | Normal | 0.18
Explosions | Normal | 0.18
Fireball | Unfriendly | 0.24
Tornadoes | Unfriendly | 0.3
Blizzard | Unfriendly | 0.3
Expose Thieves | Unfriendly | 0.36
Fool's Gold | Unfriendly | 0.42
Mystic Vortex | Unfriendly | 0.45
Nightmares | Unfriendly | 0.45
Land Lust | Unfriendly | 0.6
Meteor Showers | Hostile | 0.75

Thievery Operation | Relations Required | Value
--- | --- | ---
Free Prisoners | Normal | 0.03
Rob the Granaries | Normal | 0.06
Bribe Generals | Normal | 0.09
Bribe Thieves | Normal | 0.09
Rob the Towers | Normal | 0.09
Kidnap | Normal | 0.12
Rob the Vaults | Normal | 0.12
Steal War Horses | Unfriendly | 0.18
Incite Riots | Normal | 0.18
Night Strike | Unfriendly | 0.24
Sabotage Wizards | Unfriendly | 0.24
Destabilize Guilds | Normal | 0.24
Arson | Normal | 0.24
Greater Arson | Unfriendly | 0.3
Assassinate Wizards | Unfriendly | 0.36

### Detailed: Effects of Moving the Meter & Changing Relations

#### Normal

No Effects

#### Unfriendly

- A Dragon sent to an unfriendly Kingdom will only have 50% health points.

*Mystics:*

- Expose Thieves

- Fireball

- Lightning Strike

- Chastity

- Fool's Gold

- Nightmares

- Mystic Vortex

- Tornadoes

- Land Lust

- Abolish Ritual

- Magic Ward

- Sloth

*Thievery:*

- Night Strike

- Assassinate Wizards

- Greater Arson

- Sabotage Wizards

#### Hostile

- Some Honor gains from Ops and Spells

- A Dragon sent to a Hostile Kingdom will only have 75% health points.

- Mana costs of Offensive Spells decreases to 2%

- Stealth costs of Offensive Operations decreases to 2%

- Access to Meteor Showers

#### War

- Greatly increased Honor gains from Ops and Spells

- A Dragon sent in War has full health

- Dragon Networth Range is removed when targeting a Kingdom you are at War with

- Greatly reduced Multi-Attack Protection

- 80% Protection from hits and spell/op effects from Kingdoms outside the War (phasing in over 24h)

- Decreased Attack Time (phasing in) by 15% after 12 Ticks

*Mystics:*

- Amnesia

- War Spoils

*Thievery:*

- Propaganda

### Changelog

- Age 106: Thievery and magic meter movements updated to reflect forum changes of "all values have tripled" on 6 May 2024.

- Age 109: Failing a Raze Attack will generate 3 meter points

## Reservations

### Contents

- 1 Summary

- 2 Age Transition

2.1 Age Beginning
2.2 Age End

- 3 Respawning

- 4 Reservation Expiry

### Summary

Reservations are free spaces in kingdoms that have been reserved for particular players.

### Age Transition

When an age ends and players elect to stay with their kingdom for the next age a reservation will be created for them.

#### Age Beginning

At the beginning of a new age players who elected to stay with their kingdom will be given the option of taking up their reservation (to rejoin their teammates) or creating a new province in a random kingdom (giving up their reservation).  If a player forfeits their reservation, the reserved place in the kingdom immediately becomes a normal free space.

#### Age End

At the end of an age each province is given the opportunity to elect to stay with their kingdom for the next age.  Those that do wish to stay will have a reservation created for them in their new kingdom so they can rejoin their teammates in the next age.
3 days before age end the Kingdoms Monarch is granted the ability to extend Reservations to other players. The number of Reservations available to be granted to other players is equal to the number of empty Reservation slots in the Kingdom.
These Reservations must be accepted before the Age ends. Upon the new Age starting the players will be given the same options to use their Reservations as detailed in the above section.

### Respawning

Under normal circumstances when a province is killed the player has the option of recreating his/her province in the same kingdom. Such a player will find a reservation on the Province Lobby page upon their next visit.
If a killed province had endured multiple attacks from within its own kingdom it will not be allowed to respawn in that same kingdom.  No reservation will be created.  The player can only create a new province in a random kingdom or accept an invitation if he/she has any available.

### Reservation Expiry

Reservations typically only last for two days.  After two days the reservation will be deleted from the system.  It cannot be recovered.  This is to avoid spaces in kingdoms being reserved but unused for long periods of time.

## Runes

**Runes** are the main resource used in Spell Casting.

### Obtaining Runes

Towers generates additional runes per Utopian Day.
Runes can also be taken from an enemy province, via:

- Plunder Attack

- Thief Ops

### Decay and Destruction

After each tick, 1.2% of the total runes in storage will decay.
An enemy province's rune supply can be attacked via the Lightning Strike Spell. This attack will not give the destroyed runes to you.

## Science Formulas

Sciences are the study of knowledge and create our pathway into the future. By studying the laws that govern our being and understanding the effects of these laws, we can strengthen ourselves in all that we do. The mystery of magic and thievery, our military prowess, even our methods of production can all be enhanced through the power of study with an investment in time devoted to those fields. The students of our province will lead us into the future with your careful direction.
Mastering the Arts & Sciences makes your people stronger, smarter, and more efficient. You can grow in strength without growing in size.
Details on the benefits of different sciences can be found below.

### Contents

- 1 Science Categories, Types and Effects

- 2 Science Formula

- 3 Scientists and Books

3.1 Scientist Spawn Rate Formula
3.2 Scientist Ranks and Production
3.3 Re-assigning Scientists

- 4 Science Networth

- 5 Obsolete and historical data - saved for reference

### Science Categories, Types and Effects

Check out the Guide for descriptions: https://utopia-game.com/guide/, then go to Science in the navigation menu.

Science Category | Type | Effect | Multiplier
--- | --- | --- | ---
Economy | Alchemy | Income | ~0.0724
 | Tools | Building Effectiveness | ~0.0524
 | Housing | Population Limits | ~0.0262
 | Production | Food & Rune Production | ~0.2172
 | Bookkeeping | Wage Reduction | ~0.068
 | Artisan | Construction Time Reduction, Construction & Raze Cost Reduction | ~0.0478
Military | Strategy | Defensive Military Efficiency | ~0.0367
 | Siege | Battle Gains | ~0.0262
 | Tactics | Offensive Military Efficiency | ~0.0367
 | Valor | Reduced Military Train Time & Increased Dragon Slaying Strength | ~0.0582
 | Heroism | Draft Speed & Draft Costs Reduction | ~0.0418
 | Resilience | Reduced Military Casualties | ~0.0489
Arcane Arts | Crime | Thievery Effectiveness | ~0.1557
 | Channeling | Magic Effectiveness | ~0.1875
 | Shielding | Reduced Damage from Enemy Thievery and Magic Instant Operations | ~0.0314
 | Sorcery | Increased Magic Instant Damage | ~0.0314
 | Cunning | Increased Thievery Operation Damage | ~0.0314
 | Finesse | Reduced Wizards and Thieves lost on Failed Spells and Operations | ~0.0965

### Science Formula

**Science Bonus =** ( # of Books in Type )^(1/2.125) * Science Multiplier * Race Mod * Personality Mod * Amnesia Effect * Scientific Insights Mod * Libraries Mod

### Scientists and Books

- Each province starts with a set number of Scientists assigned to the three science Categories (Economy, Military, Arcane Arts).

- Scientists start out as Recruits, then as they progress they provide incrementally greater benefits with each progression.

- Scientist experience is based on how many Books they have produced in that category.

- Scientists have no Networth value.

- Scientists can be re-assigned at any time, but revert to Recruit level when doing so.

- Every tick each province builds progress towards a new scientist. Universities increase the rate of this progress.

- Scientists produce a set number of books each tick in the Category they are allocated (Economy, Military, Arcane Arts), based on their rank. Schools increase this effect.

- Books can be allocated to any science Type within the Category they have been produced.

- Allocated books go into effect instantly.

- Inactive provinces do not produce Books.

#### Scientist Spawn Rate Formula

**Scientists Spawn Rate =** 2 * Race Mod * Universities Effect * Revelation Mod

#### Scientist Ranks and Production

Rank | Experience | Book Production
--- | --- | ---
Recruit | 0-1439 | 60
Novice | 1440-5279 | 80
Graduate | 5280-12479 | 100
Professor | 12480+ | 120

#### Re-assigning Scientists

Re-assigning scientists drops them back to a recruit. Refer to this forum post for a discussion on this topic: http://forums.utopia-game.com/showthread.php?639982-A-Question-About-Ticks-amp-Buildings

### Science Networth

Books are worth [0.000006 * Current Land] points.

### Obsolete and historical data - saved for reference

Historical information on science systems and formulas can be found here: **Science: Obsolete and historical data**

## Scientists

The following table lists **Scientist Names**, awarded to notable members of the Utopia community in recognition of their exceptional contributions. These honors may be granted for social impact within the community — such as supporting and growing the player base — or for outstanding in-game achievements, including winning highest Honour, Land, Networth, or other competitive accolades.
*If your name appears on this list and you would like to add or update your details, please contact* **@Wiki Team Member** *on the* **MUGA Discord**, *or post your information in the* **#wiki** *channel and someone on the team will add it!*

Name | Bio | Kingdoms/Alliances | Crowns/Achievements
--- | --- | --- | ---
Abigor Boss-Brooks |  |  |
Allanon |  |  |
AmrasArFeiniel |  |  |
AquaSeaFoam (aka Jeremy) | AquaSeaFoam, often referred to as ASF, rose to prominence as one of the leaders of the Rage of Absalom kingdom. He was known for running things efficiently with minimal effort, emphasizing strategic thinking over micromanagement. ASF introduced the “cow” economy–an innovative mass-science pumping strategy to bolster kingdom-wide net worth. He became one of the first to exceed 40,000 acres and led Absalom to around 30 crowns in Utopia’s early ages. Even after stepping back from active play, he continued advising key players and kingdoms. | Absalom’s Dark Lords (and its successor kingdoms: Hand/Skies/Heart of Absalom, Beauty of Absalom, Destiny of Absalom, Rage of Absalom), Emeriti | Approximately 30 crowns led as leader of Absalom; multiple top-rank provinces and pioneering economic strategies
Arg0th |  |  |
Ari |  |  |
Ashh |  |  |
Atropine |  |  |
Auke |  |  |
Ayntheas |  |  |
Azalon |  |  |
Bahamas Royz |  |  |
Barristan |  |  |
Benjamin |  |  |
Benji |  |  |
Bijo |  |  |
Binar (aka binbin) | Began playing Utopia at around age 13, with early participation in Ages 2, 6, and 7. Known for leadership in Defiance CSB (Slaughtering Brothers Alliance) and later the VAT alliance. Experienced multiple monarch deletions by Mehul, took a break in 2005, and returned in 2007. Active in NI alliance for several ages before leading Emeriti to multiple crowns. Respected veteran with deep historical ties to the game and community. | VAT, NI, HaLL, Emeriti | Multiple crowns with Emeriti
Bishop |  |  |
Birdie |  |  |
BigCrunch |  |  |
Brian |  |  |
Brian with an I |  |  |
Caff |  |  |
Cato |  |  |
CGG |  |  |
Chadbrochill17 |  |  |
Chadde |  |  |
Chigga |  |  |
Coco |  |  |
Coolcobra |  |  |
Crescent |  |  |
Cyclops |  |  |
Cyrax |  |  |
Czarina |  |  |
DarthZejdr |  |  |
DavidC |  |  |
Devolution |  |  |
Dhamon |  |  |
Disciple |  |  |
Dorje |  |  |
Dread |  |  |
Drixx |  |  |
Dumnorix |  |  |
Elva |  |  |
Emeritus |  |  |
EvilQueen |  |  |
Ezzerland |  |  |
Fate1316 |  |  |
Fear |  |  |
Feyr |  |  |
Fisher |  |  |
Flogger |  |  |
Flutterby |  |  |
Furto |  |  |
Gearhead |  |  |
Ghetto Vets |  |  |
Gims |  |  |
GM |  |  |
Gohan |  |  |
Goldy |  |  |
Gringo |  |  |
Hawk | Hawk is also known as Hawkerz. Hawk runs the Absalom IRC server and can totally kline your ass. Nobody is sure what Hawk does for a living. He has been confirmed as a jaguar wrangler, male stripper and accountant at various times in his career. Hawk is a member of the cyberpolice. In the event that you have dun goofed, he can backtrace your ass. It is important not to dun goofed, as consequences will never be the same, including, but not limited to, a glock being popped in your mouth to make a brain slushie. |  |
Hayyie |  |  |
hengz |  |  |
Hex |  |  |
Jackmanz |  |  |
Jalgir |  |  |
Jannebananas |  |  |
Jared |  |  |
JBatts |  |  |
JeffT |  |  |
JelloJen |  |  |
Jobo |  |  |
JoRoSaR |  |  |
Joules |  |  |
Kagge |  |  |
kax0 |  |  |
Kench |  |  |
Klapptress |  |  |
Lei |  |  |
Loke |  |  |
Luthlorian |  |  |
MacLean |  |  |
Mad_Scottish |  |  |
MaGiciaN |  |  |
Mansoor |  |  |
Maranda |  |  |
Matt |  |  |
Memster |  |  |
MiKer |  |  |
Mink |  |  |
MoRon |  |  |
Mr187 |  |  |
MrJingles |  |  |
Munk |  |  |
Neil |  |  |
Ned Kelly |  |  |
Nick_Mi |  |  |
NoZ |  |  |
Nora |  |  |
Nuck |  |  |
Old Sam |  |  |
Optimus |  |  |
Owa |  |  |
Paladin |  |  |
Paladin Butters |  |  |
Palem |  |  |
Palo |  |  |
Peetah |  |  |
PersainCat |  |  |
Pestilence |  |  |
PioIsPro |  |  |
Protector |  |  |
Rasor |  |  |
Redbird |  |  |
Regulate |  |  |
Retard |  |  |
Ryshad |  |  |
Sabbot |  |  |
Sassy_Wolfie |  |  |
Scott Dryden |  |  |
Sean |  |  |
SharkX |  |  |
Shya |  |  |
Skraz |  |  |
Smiles |  |  |
Soah |  |  |
Sonja |  |  |
Sonny | Sonny was a founding member of Barcoloco, helping them to attain the first World of Legends quad crown on age 78 (along with numerous subsequent crowns). Sonny brought levity and laughter, even during the most stressful of wars, with expertly timed jokes and hysterical photoshopped images--mostly of Maugrim and Mansoor in compromising positions, a slideshow of Maugrim around the world, and Barcoloco’s infamous pub banner. He was witty and articulate, and engaged with his kingdom mates on a personal level. Sonny passed away and was awarded a post-humous scientist name by the current owners MUGA Gaming Inc at the conclusion of age 90. |  |
Spyder |  |  |
StarCop |  |  |
SteelPenguin |  |  |
Stripe |  |  |
Syntico |  |  |
Swagger |  |  |
Tadpole |  |  |
Tengil |  |  |
Thalius |  |  |
TheEyeball |  |  |
TheMango |  |  |
Tom | Tom (Zulu) is a long time member, who is part of MUGA Game Support. He devotes his time and energy to ensure the community is held to the standards set in place and helps foster a positive culture and gaming experience. | Fluffylicious, SYG, WeHurt | Age 71 Orc Land Crown
trpnhntr |  |  |
Universe |  |  |
Unos |  |  |
Vengeance |  |  |
Vir |  |  |
Wuped |  |  |
Yozz |  |  |
yourfather |  |  |
Zauper |  |  |
Zzo |  |  |

## Should my KD Predetermine a Setup 

### Introduction

- This article is largely targeted towards new kd's that are just starting to think about moving from a random setup to a predetermined setup

Every age there are changes to race/pers that ought to determine the optimal KD strat. Races, personalities, and even more nuanced changes to game mechanic change regularly. KD-wide strats are many times worth having, but depend on what you want out of the game as both a player/leader and kd.
**1.	KD-wide strats permit a KD to have a pre-determined style of game-play; one that is maximally amenable to the habits and interests of those within the KD.**
Utopia is an odd game in so far as there is no clear interpretation(for many playing) of what it means to be “winning.” At the extreme, if you are interested in pure size, then getting off to a fast start, having a race/pers that improves as your prov scales, and having a build more suited towards OOW pumping, hostile wars, and min time wars is beneficial. Embedded within any discussion as to kd-wide build is a conversation about KD goals. If you want to shoot for top 5, it should be different than if you want top 10-30 and pester top kd’s, 30-100 and war other war kd’s, or be out of the top 100 all together and just WW.
**2.	KD-wide strats allow for provinces to ensure synergy.**
**3.	You can make sure that you won’t have a glaring weakness that can be used against you during war/hostile.**
Such weaknesses may include a lack of economy, an inability to open on targets in hostile, a lack of fools gold, or a lack of provs capable of becoming UB.
**4.	Besides KD-goals, KD-wide builds can also suit your habbits better or worse. **
Just as kd-builds are associated with KD goals, they are also associated with what your preferences are, what your habits are, and what you understand to be those game mechanics most easy to capitalize on.
**5.	KD-Wide strats are not for everyone.**
KD-wide strats allow you to optimize based on what your kd wants, but sometimes what the kd wants is to simply goof around with some new race/pers that seems fun. It can be fun making strategies based around the random choices people made. Going random also synergizes well casual play, as war kd’s often want to war kd’s that seem to possess similar skill, and so a terrible setup can bait the types of wars you want.

## SoM translation

This is part of the Utopia WIKI Mini Guide Series.
---

THIS PAGE describes a game mechanism - Guide:SoM in utopia. It also aims to discuss the implications of this game mechanism & how others have utilized it. To discuss further implications or ask questions with regards to Guide:SoM, be sure to check out the discussions page. | THIS PAGE describes a game mechanism - Guide:SoM in utopia. It also aims to discuss the implications of this game mechanism & how others have utilized it. To discuss further implications or ask questions with regards to Guide:SoM, be sure to check out the discussions page.
--- | ---
THIS PAGE describes a game mechanism - Guide:SoM in utopia. It also aims to discuss the implications of this game mechanism & how others have utilized it. To discuss further implications or ask questions with regards to Guide:SoM, be sure to check out the discussions page.

### What is a SOM?

A SOM is a Spy On Military Report of a target, reflecting his military affairs page.
**You get SOMs for several reasons**

- To determine your target's defense at home (if he has armies out).

- To determine how long his army is out for.

- To determine what sort of troops your target is training.

#### How accurate is a SOM?

SOMs and other intel operations' accuracy is dependent on the number of thieves that succeed in the operation. The range of accuracy runs from +/-3% to +/-25%. To achieve the minimum of randomness 10% of the senders thieves need to gather intel on the target province.

#### What values are always accurate in a SOM?

The only values on a SOM which are always accurately reported are:

- Army out time

- Troops out on an attack

- OME, DME, Net Offense Home, and Net Defense Home

## The Plague

### Plague & Immunity

Any province, including Undead, can catch plague. Immunity prevents penalties and throne display but does not prevent carrying or spreading it. Spread occurs through both attacking and defending.
Undead normally *Always Carry and are Immune to Plague*, invisibly holding it, ignoring its effects, and spreading at the base rate (**X**). All other races that contract plague — and Undead in ages without *Always Carry* — spread it only at the reduced rate (**Y**), which lowers transmission frequency but not plague strength.

#### Effects of Plague

- No Population Growth

- −15% Income (applied as −15% Tax Collection in the formula)

- −15% Defensive Military Effectiveness

- −10% Offensive Military Effectiveness

#### Cure Mechanics

- Nature’s Blessing: 33% chance per cast to cure plague, and every tick it is active.

- Hospitals: Daily cure chance (~3% base), scaling with BE, up to 75%.
 At 100%+ BE, 25% Hospitals = max cure.
 At lower BE, more are required.

## Thievery Formulas

### Contents

- 1 Thieves Per Acre

1.1 Raw TPA
1.2 Mod TPA

- 2 Stealth

- 3 Thieves to Send

- 4 Thievery Yield

- 5 Thievery Table

### Thieves Per Acre

The ratio of your TPA to your opponent's TPA will determine the success rate of your conducted thievery ops.

#### Raw TPA

**Raw TPA =** Number of Thieves / Acres

#### Mod TPA

**Modified TPA =** Raw TPA * Invisibility * Crime Science * Racial Mod * Thieves Dens Bonus * Honor Bonus * Ritual Bonus

Modifier Type | Active | Otherwise
--- | --- | ---
Invisibility | 1.1 | 1
Ritual: Havoc | 1.2 | 1
Thievery Science | Check your science page

### Stealth

The amount of stealth you use depend on what thievery operation you use and your relations with the opposing kingdom:

- Sabotage Operations (without relations) - 3%

- Sabotage Operations (Hostile or higher relations) - 2%

- Espionage Operations - 2% (excluding Spy on Throne and Spy on Defense, which are 1%)

You need at least 5% stealth to be able to send your thieves out.
If you log on to find your stealth being much lower than you expected, someone has probably cast Expose Thieves on you. The spell will reduce your amount of stealth to 95% of what you had each tick, before regen.
Stealth increases with 3% every hour (excluding personality or racial bonuses).

### Thieves to Send

**Optimal Thieves to Send =** (Opponents' Resources * Max % Of Total) / Gains Per Thief / Racial Mod

- Opponents' Resources can be found by using the Spy on Throne thievery op.

- Max % of Total and Gains per Thief are given by the table below.

### Thievery Yield

**Thievery Yield =** Thieves Sent * Relative Size * Gains Per Thief * (1 - Resources Lost) * Racial Mod * Personality Mod * Science Mod * Guile
**Relative Size =** *MIN* ( Target Networth / Self Networth , Self Networth / Target Networth) + War Bonus

- Gains Per Thief is given by the table below.

- Resources Lost is given by the table below.

- Thievery Yield is reduced by up to 62.5% by watch towers.

### Thievery Table

Out of war
---
Maximum Gains | Rob Granaries | Rob Vaults | Rob Towers | Kidnap Peasants | Steal Horses | Night Strike
Max % of Total | 37.5% | 5.20% | 21.3% | 1.85% | 12.75% | 18%
Gains Per Thief | 53.55 | 40 | 17.5 | 0.132 | 9.4% | 90%
Resources Lost | 10% | 10% | 10% | 20% | 50% | 0

At War
---
Maximum Gains | Rob Granaries | Rob Vaults | Rob Towers | Kidnap Peasants | Steal Horses | Night Strike
Max % of Total | 40% | 13.6% | 28% | 4% | 13.6% | 16%
Gains Per Thief | 96 | 64 | 16.8 | 0.285 | 10% | 80%
War Bonus | 25% | 25% | 25% | 25% | 25% | 25%
Resources Lost | 10% | 10% | 10% | 20% | 50% | 0

## Time in Utopia

Each event in Utopia is dated in **Utopian Time**.

Utopian Chronology
Time in Utopia moves differently to the real world. Each Age consists of Days, Months and Years.
The start of each Utopian Day is called a tick.

    1 Utopian Day = 1 Hour
    1 Utopian Month = 1 Day
    1 Utopian Year = 1 Week

Before Age begins, there is a Freeze time.
The Age starts at January 1, Year 0 with Protection until February 1, Year 0. As a rule Age continues 8..14 Utopian Years.
Time in Utopia is synchronized with time in real world. Each Utopian Day begins in XX:00. Utopian Month changes at 18:00 GMT+0 timezone.
Typical Utopian data format:

- February 5 of YR4

Tick
Tick is an unique unplayable time between every Utopian Days, when most of bonuses and penalties are applied to Province.
During the tick mana and stealth recover, people are born and die, armies and wizards are trained, inhabitants consume bushels and money, banks emit gold coins, etc.
Note that there is an order of operations for each Tick. Below, I attempt to order them:

- Buildings are built first at the beginning of the tick and will affect the below:

- Income is generated

- Food is generated

- Peasant growth

- Wizard growth

- Drafting occurs

Questions:

- Does "-" count as a tick for Patriotism or not (effectively, it seems to be the case that a spell that says 18 days is then really 19, which is kind of disorienting).

Some notes in this forum post: http://forums.utopia-game.com/showthread.php?639982-A-Question-About-Ticks-amp-Buildings

Utopian Calendar
In Utopia terms there are 24 days in a month and 7 months in a year.

  Utopian Year Calendar:

    **January**
        1   2   3   4   5   6   7   8
        9   10  11  12  13  14  15  16
        17  18  19  20  21  22  23  24
    **February**
        1   2   3   4   5   6   7   8
        9   10  11  12  13  14  15  16
        17  18  19  20  21  22  23  24
    **March**
        1   2   3   4   5   6   7   8
        9   10  11  12  13  14  15  16
        17  18  19  20  21  22  23  24
    **April**
        1   2   3   4   5   6   7   8
        9   10  11  12  13  14  15  16
        17  18  19  20  21  22  23  24
    **May**
        1   2   3   4   5   6   7   8
        9   10  11  12  13  14  15  16
        17  18  19  20  21  22  23  24
    **June**
        1   2   3   4   5   6   7   8
        9   10  11  12  13  14  15  16
        17  18  19  20  21  22  23  24
    **July**
        1   2   3   4   5   6   7   8
        9   10  11  12  13  14  15  16
        17  18  19  20  21  22  23  24

## Traditional march

Types of Attacks
---
Attacks | Effects
Traditional March | This attack, if successful, takes away a portion of the target's land (base ~12%), and gives it to the attacker when his/her army returns. The target's size in Acres and Relative Networth are factored in to determine the amount of land taken.
Raze | This attack, if successful, destroys a portion of the target's land (~5%). During war, this attack only destroys buildings (~30%).
Plunder | This attack, if successful, will steal a portion of the target's money, food and runes, and deliver it to the attacker.
Learn | This attack, if successful, will steal a portion of target's allocated books. Base gains are (~2%) plus a portion (~2%) of the target's unallocated books.Part of the stolen allocated books will be destroyed. A portion of the stolen allocated books will become unallocated for the source to re-allocate. During War, Learn temporarily removes ~30% of current allocated Science Books, these return over 48 Ticks.  Book return over 48hrs not affected by EOWCF
Massacre | This attack, if successful, will kill a small percentage of the target's peasants, thieves and wizards. Greatly enhanced in War.
Conquest | This attack, like Traditional March, will, if successful, take away a portion of the target's land and give it to the attacker. However, the attacker is only required to send 51% of the target's defence to be successful. The land gained, on the other hand, will be significantly lower than Traditional March. Sending more than 51% will return higher gains up to a certain limit.Available only within 5% Networth range outside Hostile/War, unless attacker has access to Enhanced Conquest
Ambush | This attack can only be performed against a target which has recently attacked the province seeking to ambush with a successful land attack, and whose army has not yet returned home. If successful, this attack will return 50% of the acres stolen. The defending army will defend at only 80% efficiency, and no other military modifiers are taken into account. Offensive specialists defend at the normal defensive strength of their defense specialists. Inflicts 15% increased Military Casualties.Neither Anonymous Attacks or War Spoiled Attacks can be ambushed, and you cannot Ambush a failed hit.

### Additional Information

- Attacking & Calculating an Attack

- Attacking & Defending

- Military

- War

## War Score

As of Age 102, War Win Point System has returned.

- The war win point system will be largely hidden. It will be a three stage calculation system.

- The initial war win points will be awarded as follows:
Win = 2 points
Mutual Peace = 1 point
Loss = 0 points

- After the conclusion of the age, kingdoms will be awarded bonus war win points for every kingdom that they defeated in war, based on  the defeated kingdoms' total war wins (if any).

- Finally, as a soft adjustment, an additional provision of points will be granted for every kingdom warred but not defeated, based on the total war wins of those kingdoms (if any).

- Kingdom pages will still only show the number of war wins (along with the war history), with war win points determining the final standings of kingdoms after age concludes.

- Failed Attacks will increase the GBP/MAP of the defender, based on relative offense sent/defense, linearly scaling from 0 to half the amount of GBP/MAP generated on a successful Traditional March.

As of Age 103,

- War Score will now incur a stacking 2% penalty for each missing province below maximum (calculated for each individual War, this carries over to EoA adjustment, full points only awarded full kingdoms).

## Warleader Guide to Attrition

### Contents

- 1 An advanced war leader’s guide to attrition and winning hard wars

- 2 How wars are won

2.1 Attrition levers
2.2 Natural attrition (~15% of military per 24h)
2.3 Hitting Ratios
2.4 Nightstrike/Propaganda (12% per 24H + 15% from initial stealth bank)
2.5 Meteor Showers (~15% enemy defence, which is typically ~6%-6.5% total military per 24H)
2.6 Chaining (~6.5% total military per 24 hrs)
2.7 Military Efficiency
2.8 Rituals (~4% off/def per 24H)
2.9 Steal Warhorses (1%-1.5%)
2.10 Hitting Leets on their defensive value
2.11 GBP/MAP
2.12 Setup (Races, builds, Science, leets%)
2.13 Spells
2.14 Redrafting (up to 30%-35% of Peons per 24H)

### An advanced war leader’s guide to attrition and winning hard wars

This guide is designed for experienced (or aspiring) war leaders with substantial experience in warring. It is not a beginner’s guide and assumes good game knowledge. While there are some materials for the beginner and mid-tier player, there is almost no body of knowledge for the war leader aspiring to move from the medium-high tier to the highest level of the game. While the specific balance will change from age to age, I imagine the overall approach embedded in this guide will remain relevant.

### How wars are won

Wars are won when one kd goes under 66% of the NW of the other kds. Withdrawing is just a way to fast forward the process; the only way to actually secure a win is to forge an unopposable path to auto-win. There are 3 main ways to achieve a win:
(1) Ub wall: non-land NW attritions at ~30% per 24h, so if you can create a significant advantage (5-10 provs more than the other kds) in untouchable or very hard to damage provs (ones that will generally be keeping or gaining nw), the rest of the war will keep clashing into each other until these provs hold a big chunk of NW enabling a win. This is great when you can achieve it. If you made this happen in the first 6 days of war the war was never close.
(2) Brute force: If your hitting output is substantially higher than the other KD (e.g you are running 25 +gains/fast attackers vs a hybrid kds) you can sometimes just hit your way to autowin. This happens mostly in OOP wars and niche situations.
(3) Down, Down, Down and up again (AKA: attrition): The main way hard wars are actually won is by compressing the militaries. If a war starts at 1M vs 950K troops - that is basically a wash. If you reduce the military down to 150K vs 100K, it becomes an overwhelming advantage, which in turn lets you take and hold the majority of the land in the war, which late in a war is the majority of the NW, and thus a path to autowin.
Since most hard wars are won by attrition, it is well worth optimising attrition to make sure that when the militaries are squeezed into tiny sad things you will remain with a small but overwhelming advantage. This guide details the various levers which typically affect attrition and their relative importance and power.
One major caveat to this is that while Kd vs Kd stats and attrition are important, they are only one aspect of a war. In most wars economy, tm power and how offence and defence are distributed within provinces are just as important as overall kd stats. In other words, not all (or even most) decisions should be guided by kd wide attrition, it is just an important aspect and relative pricing mechanisim to keep in mind when devising and executing on war strategies.

#### Attrition levers

- Natural attrition (~15%)

- Hitting ratios (++++)

- Nightstrike/Propaganda (12%)✦

- Chaining (6.5%)✦

- Military Efficiency (+++)✦

- Meteors (6%-7%)

- Rituals (4%)

- GBP/MAP (4%)

- Steal Warhorses (1%-1.5%)

- Hitting Leets on defence (++)✦

- Setup - buildings, racial bonuses, science (++)

- Spells (+)

- Repopulation (+++)

% - Estimate total impact of effect at 100% utilization (% of military per 24h)
+ - Relative importance (More + = bigger), where % is irrelevant or varies meaningfully
✦ - Direct impact on enemy offence (most attrition you control is enemy defence)

#### Natural attrition (~15% of military per 24h)

Attrition is oppositional - offence attritions vs enemy defence and vice versa. The two oppositional attrition wars happen almost entirely independently from each other. In other words, reducing enemy defence is equivalent to increasing my offence, but does not greatly affect my defence or enemy offence.
Offensive troops will drop by ~15% (7% * 2.2 waves * modifiers) per 24h. Defence troops drop at ~11% * enemy hitting ratio (5% * 2.2 waves * enemy hitting ratios * modifiers) per 24h. In most wars hitting ratios are above 1.5 so in most wars defence drops slightly faster than offence. Counter to common thinking attrition is not majorly affected by speed; as the attrition happens on both sides of the opposition, speed will only change the relative power within your kd, and the relative importance of natural attrition vs everything else happening in the war, but not the overall hitting ratio. In other words your avians will loose offence faster than your dorfs, but all your attackers vs all enemy defence will not drop faster in a kd runing avians.
Overall natural attrition is directly affected by builds, science, spells, speed, racial bonuses, rituals and micro tactics. While there are many modifiers, 15% of total military is a useful order of magnitude baseline to compare natural attrition to other things for the purpose of understanding the relative importance of the other attrition levers.

#### Hitting Ratios

Hitting ratios are the practical-offense:practical-defence of the opposing kd. A hitting ratio of 1 (kd practical offence = other kd practical defence) means you will be able to make ~25 average hits per wave. With a hitting ratio of 2 you will be able to make 50 average hits per wave.
A hitting ratio delta not only says who will be able to do more damage directly at the start, it is also exponential because a high hitting ratio means enemy defence drops faster - a kd with double the hitting ratio hits defence twice as many times per wave, so as a % of your offence loss enemy defence drops twice as fast, which further increases the hitting ratio.
Hitting ratios are also the main determinant of the pattern of a war and the speed of natural attrition vs all other attrition. Wars with very low hitting ratios (<1.2-1.3) will see offences disappear fast, ubs emerge early, a tm heavy war, and both kds struggling to keep offence. Wars with particularly high hitting ratios (2.5+) will see defence drop much faster and economies wrecked. Typical wars are in the middle.

#### Nightstrike/Propaganda (12% per 24H + 15% from initial stealth bank)

If 25 provs manage to NS at ~80% success rate against a good mix of provs in range with low GBP and typical wt’s (GA’ed to 8%-10%) and a decent mix of spec/leets, this leads to an order of magnitude of 15% troop removal from an initial 100% stealth + ~12% per 24 hrs. You can theoretically go a higher with troop concentration, many rogues, high spec armies, little/no wt’s or etc’, but 12% is pretty much the upper bound of practical possibility with 25 thievery able provs. Of course, it is almost never the case you can NS with 25 provs @ 80% success. A useful way to approach NS effect on attrition is to look at dNS between kds as a % of theoretical utilization. If you have 12 provs NS’ing, and other kd has 6 provs NS’ing at a comparable success rate, you will have 25% dNS =~ 3% delta troop removal per 24 hrs or roughly 20% boost to natural attrition. Prop is within the same order of magnitude as NS for the purpose of military number changes

#### Meteor Showers (~15% enemy defence, which is typically ~6%-6.5% total military per 24H)

24/7 full MS cover ~doubles natural defence attrition. If there are provs you can’t or don’t MS, you lose their proportion of difference (MS does most when landed on tms / turtles).

#### Chaining (~6.5% total military per 24 hrs)

Chaining is useful because it is one of the only ways for attackers to remove enemy offence (whereas natural attrition targets enemy defence). If you perfectly deep chain 4 provs per 24 hrs you can expect to remove ~40% on average of their military via overpop, thus the excess damage from overpop will be ~6.5% of enemy kd military (4/25*0.4) per 24 hrs (enemy provs will loose more, but much of that was natural attrition from the hits). Deep chaining is one of the strongest tactical tools in the game, but it is surprisingly inefficient for attrition purposes. You generally only remove the overpop from when the prov is first rioting until the army comes home (same as semi-chaining) because when the army gets home the other prov is going to release and aid/retrain, so you are moving rather than destroying troops. The overpop is also offset by hitting into maximum GBP, and often protective spells (WS,Salvation, GP). The attrition value of chaining can be slightly raised by semi-chaining more provs (at the cost of being less useful tactically).

#### Military Efficiency

ME affects troop loss linearly. 200 OME means you lose half as many troops to break the same defence. This is particularly important in wage drops. If one kd has stronger econ control and can force the other kd to drop wages (e.g 100% avg vs 200% wage =~ 12% delta ME), the other kd will not only lose offence and defence, they will also lose more troops per hit, thus expanding the overall gap for as long as the wage discrepancy remains, even if it is later removed.
It is worth noting that temporary ME changes affect natural attrition, while permanent ME affect everything except natural attrition. For example, if I MV a MP+GP to temporarily reduce DME right before a hit, the hit prov will lose 10% more defence per offence point sent. Permanent ME by comparison does not impact natural attrition: a warrior (e.g. +12% OME) will always lose 12% fewer offensive troops, but the lost troops would have hit 12% harder, so the ratio of attrition in off/deff terms remains constant. However, NSing a warrior which enjoyed higher ME does more to the top line, so the higher the ME of a kd, the less important natural attrition is on a relative basis to all other troop removal mechanisms.

#### Rituals (~4% off/def per 24H)

Stalwart & Onslaught both create a 27%-29% delta multiplicative to one side of natural attrition. 26% direct Delta comes from 10% OME/DME * 15% extra/under losses. There is also an additional smaller indirect effect driven by the change to hitting ratios due to the ME change. Rituals are a large effect, so in close attrition-driven wars a kd able to keep airtight ritual coverage while creating gaps in the other kds ritual will often end up winning.
Onslaught and Stalwart have very similar effects on attrition. Which of the two you choose for the 2nd/3rd/4th ritual of a war should be determined primarily by whether you want hitting ratios to increase or decrease. Broadly speaking - the kd with a tm advantage wants to reduce the relative importance of natural attrition and hits to give more relative power to their tms, and ergo will want stalwarts; whereas a kd with a tm disadvantage will want onslaughts for the opposite reasons.

#### Steal Warhorses (1%-1.5%)

War horses typically add 15%-20% offence. Systematically stealing horses is a temporary measure, equivalent to a temporary reduction in OME, a practical steal of 75% of enemy horses thus results in a 10%-15% loss of offence, and  an equivalent boost to natural attrition while the horses repop. If you also destroy the stables this becomes kinda permanent in most wars.

#### Hitting Leets on their defensive value

A typical attacker elite with e.g 14/3 (25/4 mod) dies ~6 times as fast using its defensive value. Every time you hit attacker elites on their defence value they drop like flies. This can be done with ambush or by hitting elites home.
Ambush is nice but capped because you can only hit each elite once. Catching elites home is the main tool here and is most significant in already heavily hit provs with low defence, so you are able to 4X and remove 20%-25% of enemy leets in one fell swoop. If you are able to do this and GBP is low, consider raze bouncing (send 96% to max damage without breaking) the first hits to keep GBP low for as many hits as possible.

#### GBP/MAP

Maxed GBP/MAP offers ~37% attrition difference (-30% troop loss + temporary ME boost). Whilst you often sort of have to hit into maxed GBP in war, Paying attention to GBP in target and hit selection, both in hitting low GBP provs, and in keeping your GBP up for as long as possible after hits (e.g raze before trad) can really add up.

#### Setup (Races, builds, Science, leets%)

Racial bonuses affect attrition broadly the way you would expect, but often less than you would expect unless a concentrated effort is made. Multiply natural attrition X the bonus X the proportion of your KD’s offence/defence covered by the bonus to get an order of magnitude of it’s total effect. It is worth noting defensive racial bonuses can kind of be sidesteped (i.e I will chain/NS clerics, while I will let non-clerics attrition naturally), whereas offensive ones cannot be avoided. Hence +kills is generally better than -loss.
Hospitals affect attrition the way you would expect. TGs & Forts affect attrition pretty much linearly to the bonus (with small additions to hitting ratio impact). It is reasonable to think of them as having a secondary impact as off/deff only hospitals. All building-based attrition modifiers are semi-temporary because they tend to fall off a cliff on day 2-4 of a war when all the peons die and all the acres get razed.
Resilience science affects attrition how you would expect. The main point of note is that resilience tends to be higher on attackers, so later in the age as resilience rises natural attrition of defence gets faster than offence generally speaking, resulting in a general acceleration of hitting ratios as wars go on later in the age.
Leet% effects attrition in a few ways. At a basic level specs convert to elites thus creating an offence regeneration mechanism. As a side effects having a high % of specs reduces the effect of chains (cheaper to release), increases the effect of NS (die faster) and reduces the effect of bushes and catching armies home.

#### Spells

Spells affect attrition broadly how you would expect.
BL has a 22% attrition delta (you kill 26% more but only lose 4% more, as the ME is multiplicative with the losses).
MP+GP have a 5% impact as expected.
WS & Salvation each have a ~10% of total natural attrition impact (covering the entire kd 24/7 changes total Delta troops by ~1.5% of total military per 24 hrs). In most setups and most wars they are not worth covering but are very good on specific targets or if you are set up specifically to cover them..

#### Redrafting (up to 30%-35% of Peons per 24H)

Somewhere around day 5-9 in very intensive wars (earlier in less intensive wars or early in the age), redrafting becomes the most important factor in attrition. The most important indicator here is military unit:peons (not peon per acre). The ratio impact varies situationally but a decent rule of thumb for mid age:
20+ military:peon → no drafting, wages brutally reduced.
10-20 military:peon →  almost no drafting, severely reduced wages
5-10 military:peon → minor drafting, minor struggle to keep wages paid.
2-5 military:peon → drafting will be ~1%+ and wages can be paid with minor coordination
2 or less military:peon → Draft will be 1.5%-2% of peons.
If we assume total military attrition to be ~25-30% of military per 24 hrs, drafting becomes very significant at 4-5:1 military:peon and there is a “break even” point where military count starts going up somewhere around 2:1 military:peon.

**Credits: just me of CoL**

## Wizards

### Contents

- 1 Units

- 2 Formulas

2.1 Soldiers Drafted Per Tick
2.2 Draft Cost Formula
2.3 Draft Rate Formula
2.4 Training Formulas
2.5 Maintenance cost

### Units

Here are the unit types that are available in Utopia (racial/personality bonuses are not included)
---
Units | Description | Offense | Defense | Cost | Networth
Peasants | Peasants are responsible for working and generating income for your province. |  |  |  | 0.25
Soldiers | The basic unit for every province. They are drafted from Peasants and can be trained into Specialists, Elites or Thieves. You are not required to pay Wages for Soldiers. | 3† | 0† | Varies | 0.25 networth per point of power
Wizards | Wizards are required to cast spells. They do not count towards your military size. Check out the Mystics Guide as well as the Mystic Formulas. |  |  |  | 7
Thieves | The part of your military which will conduct Thievery ops. Be sure to check out Thievery Formulas as well |  |  | 500gc | 5
Horses | Sending horses with your attacks adds raw offensive point per horse. You may include up to one horse per military unit sent in combat. | 2† |  |  | 0.3 per point of power
Prisoners | Prisoners are taken from the total number of enemies that would've been killed after an attack, usually at a 2/3 prisoner to total kills ratio - IF there is room in your dungeons for them. Prisoners have no upkeep, every 2 prisoners fills 1 job, and every prisoner produces 0.75gc per hour. About one third of the prisoners sent are lost in the fight. They are then again immediately available to your general. You can use at most 1 Prisoner for every 5† normal troops you send. | 8† |  |  | 0.2 per point of power
Mercenaries | You can use at most 1 Mercenary for every 5† normal troops you send. | 8† |  | 300gc |
Defensive Specialist | These troops defend your land only, and are unable to attack. |  | 10† | 350gc | 0.5 networth per point of power
Offensive Specialist | These troops are used to attack, and are unable to defend. | 10† |  | 350gc | 0.4 networth per point of power
Elites | Elites have offensive as well as defensive strength. Their offensive and defensive values vary from race to race. For Elite values please see the respective Race page. | Varies | Varies | Varies | Varies

† Race and Personality modifiers can increase or decrease this number.

### Formulas

#### Soldiers Drafted Per Tick

**Soldiers Drafted per Tick =** Peasants * Draft Speed * Race Bonus * Personality Bonus * Patriotism * Affluent Ritual * Sloth * Dragon * Heroism Science Effect

Modifier Type | Active | Otherwise
--- | --- | ---
Patriotism | 1.3 | 1
Sloth | 0.5 | 1
Ruby Dragon | 0.75 | 1
Expedient Ritual | 1.2 | 1

#### Draft Cost Formula

**Cost of Soldier Drafting =** Current Draft Level Factor * Draft Rate * Race Bonus * Personality Bonus * Armouries Mod * Heroism Science Effect * Sloth Effect

**Note**

- Current Draft Level Factor scales base soldier draft cost upwards once 50% of max population is reached

- Draft Level Factor is MAX(1.0154*((Solds+Ospecs+Dspecs+Elites)/maxpop)^2+1.1759*((Solds+Ospecs+Dspecs+Elites)/maxpop)+0.3633,1)* base rate for level

#### Draft Rate Formula

**Draft Rate =** Base Draft Rate * Patriotism Bonus * Heroism Science Effect * Sloth * Ritual

- Drought reduces draft rate by 15%

Base Draft Rate | Draft Speed | Cost per soldier
--- | --- | ---
Reservist | 0.5% | 30gc
Normal | 1.0% | 50gc
Aggressive | 1.5% | 75gc
Emergency | 2.0% | 110gc

#### Training Formulas

**Training Cost =** Unit Cost * Race Bonus * Armouries Bonus

**Full training time =** 24 * Race Bonus * Personality Bonus * MAX (Inspire Army,Hero's Inspiration) * Valor Science Effect * Haste Ritual * Training Grounds Bonus

#### Maintenance cost

**Click here for the Formula**
