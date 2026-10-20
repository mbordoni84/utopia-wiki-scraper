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
