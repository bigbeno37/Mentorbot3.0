import json

# Character names, sidebar colors, emote IDs, and embed icons
characters = {
    'Zetterburn': {
        'color': 16742462,
        'emote': '<:Zetterburn:547189111052566556>',
        'icon': 'https://i.imgur.com/aqLqIbB.png'
    },
    'Forsburn': {
        'color': 8744800,
        'emote': '<:Forsburn:547189098859986984>',
        'icon': 'https://i.imgur.com/wLU8CEL.png'
    },
    'Clairen': {
        'color': 15870306,
        'emote': '<:Clairen:547182529837400081>',
        'icon': 'https://imgur.com/hfcf0vb.png'
    },
    'Orcane': {
        'color': 4812504,
        'emote': '<:Orcane:547182506584047618>',
        'icon': 'https://imgur.com/uF2DuY7.png'
    },
    'Etalus': {
        'color': 6728666,
        'emote': '<:Etalus:547182495964069898>',
        'icon': 'https://imgur.com/89ry8PT.png'
    },
    'Ranno': {
        'color': 379087,
        'emote': '<:Ranno:547182486971613185>',
        'icon': 'https://imgur.com/XNggZrr.png'
    },
    'Kragg': {
        'color': 5866833,
        'emote': '<:Kragg:547182475835736155>',
        'icon': 'https://imgur.com/qsnG9Xy.png'
    },
    'Maypul': {
        'color': 8439641,
        'emote': '<:Maypul:547182462015504404>',
        'icon': 'https://imgur.com/womvfUo.png'
    },
    'Sylvanos': {
        'color': 9082654,
        'emote': '<:Sylvanos:547182436161945601>',
        'icon': 'https://imgur.com/DUvl1o8.png'
    },
    'Wrastor': {
        'color': 10702538,
        'emote': '<:Wrastor:547182420462665738>',
        'icon': 'https://imgur.com/YQrYfuv.png'
    },
    'Absa': {
        'color': 15372270,
        'emote': '<:Absa:547182403144384532>',
        'icon': 'https://imgur.com/y0x3uUH.png'
    },
    'Elliana': {
        'color': 12151190,
        'emote': '<:Elliana:547182393908396052>',
        'icon': 'https://i.imgur.com/SIFBYfg.png'
    },
    'Ori': {
        'color': 13041407,
        'emote': '<:Ori:547182375956774920>',
        'icon': 'https://imgur.com/uTV41fW.png'
    },
    'Shovel Knight': {
        'color': 15774989,
        'emote': '<:ShovelKnight:547182360219746349>',
        'icon': 'https://imgur.com/2BvZbjO.png'
    }
}

# Rivals regions
regions = ['WestCoast', 'Midwest', 'EastCoast', 'Europe',
           'Australia', 'SouthAmerica', 'Asia', 'Africa']

absaJson = "{\"weight\":1.1,\"groundFriction\":0.63,\"dash\":{\"initial\":{\"speed\":4,\"time\":8},\"speed\":6.25,\"stopTime\":4,\"turn\":{\"time\":10,\"deceleration\":1.5},\"attack\":{\"hit1\":{\"startup\":6,\"active\":{\"from\":7,\"to\":9,\"frames\":3},\"damage\":3,\"angle\":361,\"knockback\":{\"base\":6,\"scaling\":40},\"priority\":2,\"hitstunModifier\":1,\"hitpause\":{\"base\":3,\"scaling\":0},\"angleFlipper\":0,\"killsProjectile\":true},\"hit2\":{\"startup\":12,\"active\":{\"from\":13,\"to\":15,\"frames\":3},\"endlag\":{\"hit\":18,\"whiff\":27},\"FAF\":43,\"damage\":8,\"angle\":361,\"knockback\":{\"base\":6,\"scaling\":40},\"priority\":2,\"hitstunModifier\":1,\"hitpause\":{\"base\":0,\"scaling\":0},\"killsProjectiles\":true}}},\"walk\":{\"speed\":3,\"acceleration\":0.2,\"turnTime\":6},\"waveland\":{\"friction\":0,\"time\":6},\"air\":{\"fallSpeed\":{\"max\":8,\"fastFall\":12},\"speed\":{\"acceleration\":0.4,\"max\":6},\"friction\":0.04,\"gravity\":{\"acceleration\":0.3,\"hitstunAcceleration\":0.45}},\"jump\":{\"startTime\":5,\"speed\":{\"normal\":7.6,\"shortHop\":4.5,\"maxHorizontal\":8}},\"doubleJump\":{\"amount\":0,\"speed\":1,\"acceleration\":-1.4},\"wallJump\":{\"speed\":{\"vertical\":7,\"horizontal\":6}},\"airDodge\":{\"startup\":2,\"active\":12,\"recovery\":12,\"speed\":8},\"pratFallAcceleration\":0.4,\"landTime\":{\"normal\":4,\"prat\":16},\"parry\":{\"startup\":2,\"active\":8,\"recovery\":20},\"roll\":{\"startup\":3,\"active\":14,\"speed\":9.5,\"recovery\":12},\"tech\":{\"active\":14,\"recovery\":12,\"roll\":{\"startup\":8,\"active\":12,\"speed\":8,\"recovery\":12}},\"hurtbox\":{\"height\":{\"idle\":59,\"crouch\":36,\"hitstun\":59},\"width\":{\"idle\":42,\"crouch\":42,\"hitstun\":42}},\"jab\":{\"hit1\":{\"startup\":3,\"active\":{\"from\":4,\"to\":6,\"frames\":3},\"endlag\":{\"hit\":15,\"whiff\":15},\"FAF\":22,\"damage\":3,\"angle\":70,\"knockback\":{\"base\":4,\"scaling\":0},\"priority\":2,\"hitstunModifier\":1,\"hitpause\":{\"base\":4,\"scaling\":0},\"angleFlipper\":6,\"killsProjectiles\":true,\"notes\":\"If jab is held 1 frame prior to the next part of Absa's jab loop the next hitbox will become active on the next frame, technically making the startup of her jab loops 0. If you hit another character or object at any time during the jab loop, Absa will be able to cancel into a turnaround tilt at any point in the loop afterwards.\"},\"hit2\":{\"startup\":13,\"active\":{\"from\":14,\"to\":16,\"frames\":3},\"endlag\":{\"hit\":15,\"whiff\":15},\"FAF\":32,\"damage\":4,\"angle\":361,\"knockback\":{\"base\":4,\"scaling\":0},\"priority\":1,\"hitstun\":1,\"hitpause\":{\"base\":5,\"scaling\":0},\"angleFlipper\":6,\"killsProjectiles\":true,\"notes\":\"Jab 2 loops back into Jab 1. If jab is held 1 frame prior to the next part of Absa's jab loop the next hitbox will become active on the next frame, technically making the startup of her jab loops 0. If you hit another character or object at any time during the jab loop, Absa will be able to cancel into a turnaround tilt at any point in the loop afterwards.\"}},\"neutral\":{},\"forward\":{\"tilt\":{\"hit1\":{\"startup\":7,\"active\":{\"from\":8,\"to\":11,\"frames\":3},\"endlag\":{\"hit\":12,\"whiff\":18},\"FAF\":30,\"damage\":6,\"angle\":70,\"knockback\":{\"base\":7,\"scaling\":30},\"priority\":4,\"hitstun\":1,\"hitpause\":{\"base\":8,\"scaling\":20},\"angleFlipper\":0,\"killsProjectiles\":true,\"notes\":\"Cancellable into F-Tilt 2 during frames 15-20\"},\"hit2\":{\"startup\":12,\"active\":{\"from\":28,\"to\":29,\"frames\":2},\"endlag\":{\"hit\":17,\"whiff\":28},\"FAF\":58,\"damage\":4,\"angle\":85,\"knockback\":{\"base\":9,\"scaling\":25},\"priority\":3,\"hitstunModifier\":0.5,\"hitpause\":{\"base\":6,\"scaling\":0},\"angleFlipper\":0,\"killsProjectiles\":true,\"notes\":\"Has 28f of endlag on hit1 and hit2 whiff, 22f of endlag on hit2 whiff only\"}}},\"back\":{},\"up\":{\"tilt\":{\"hit1\":{\"startup\":10,\"active\":{\"from\":11,\"to\":12,\"frames\":2},\"damage\":10,\"angle\":80,\"knockback\":{\"base\":8,\"scaling\":70},\"priority\":4,\"hitstunModifier\":1,\"hitpause\":{\"base\":8,\"scaling\":40},\"angleFlipper\":6,\"killsProjectiles\":true,\"notes\":\"Center hitbox\"},\"hit2\":{\"startup\":10,\"active\":{\"from\":11,\"to\":12,\"frames\":2},\"damage\":10,\"angle\":80,\"knockback\":{\"base\":8,\"scaling\":70},\"priority\":5,\"hitstunModifier\":1,\"hitpause\":{\"base\":8,\"scaling\":40},\"angleFlipper\":6,\"killsProjectiles\":true,\"notes\":\"Above hitbox\"},\"hit3\":{\"startup\":12,\"active\":{\"from\":13,\"to\":17,\"frames\":5},\"endlag\":{\"hit\":9,\"whiff\":14},\"FAF\":32},\"damage\":4,\"angle\":90,\"knockback\":{\"base\":6,\"scaling\":35},\"priority\":1,\"hitstunModifier\":1,\"hitpause\":{\"base\":6,\"scaling\":20},\"angleFlipper\":6,\"killsProjectiles\":true,\"notes\":\"Late hitbox\"}},\"down\":{\"tilt\":{\"startup\":5,\"active\":{\"from\":6,\"to\":11,\"frames\":6},\"endlag\":{\"hit\":9,\"whiff\":14},\"FAF\":26,\"damage\":7,\"angle\":30,\"knockback\":{\"base\":7,\"scaling\":45},\"priority\":1,\"hitstunModifier\":1,\"hitpause\":{\"base\":7,\"scaling\":60},\"angleFlipper\":0,\"killsProjectiles\":true}}}"

absa = json.loads(absaJson)

absa_template = json.load(open('/src/data/absa.json'))
