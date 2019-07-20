import random

looking_direction = ['up', 'down', 'straight', 'left', 'right']
opposites = [['up', 'down',], [ 'left', 'right']]
head_wears = [
    'viking helmet',
    'dapper hat', 'pirate hat', 'beanie', 'baseball cap', 'crown', 'hoodie', None]
emotions = ['happy', 'sad', 'angry']
mouths_emotions = ['smiling', 'numb', 'sad', 'screaming']
hair_styles = ['long top, short side', 'long', 'long hair, bun', 'long hair, hanging', 'skinned']
beard_styles = [None,
                'Long sideburns that connect to a mustache',
                'A vertical line of hair across the chin',
                'A beard with no mustache that circles the chin',
                'A mustache that covers your entire top lip',
                'A short beard with thin, neatly trimmed sides',
                'A pointed beard that traces the jawline, paired with a mustache',
                'viking beard',
                'Flared sideburns paired with a horseshoe mustache']
ages = ['young', 'old']
def main():
    first_direction = random.choice(looking_direction)
    second_diretion = random.choice(looking_direction)
    head_wear = random.choice(head_wears)
    emotion = random.choice(emotions)
    mouth = random.choice(mouths_emotions)
    hair = random.choice(hair_styles)
    beard = random.choice(beard_styles)
    age = random.choice(ages)

    while second_diretion is first_direction:
        second_diretion = random.choice(looking_direction)

    print 'age:', age
    print 'head direction:' ,first_direction, second_diretion
    print 'head wear:', head_wear
    print 'emotion:', emotion
    print 'mouth:', mouth
    print 'hair:', hair
    print 'beard:', beard


if __name__ == '__main__':
    main()