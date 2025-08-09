import random
from django.core.management.base import BaseCommand
from own_models.custom_user_models import CustomUser

# 一些常见英文名列表
ENGLISH_NAMES = [
    "Oliver", "George", "Harry", "Jack", "Jacob", "Noah", "Charlie", "Muhammad", "Thomas", "Oscar",
    "William", "James", "Henry", "Leo", "Alfie", "Joshua", "Freddie", "Archie", "Ethan", "Isaac",
    "Alexander", "Joseph", "Edward", "Samuel", "Max", "Daniel", "Arthur", "Lucas", "Mohammed", "Logan",
    "Theo", "Harrison", "Benjamin", "Mason", "Sebastian", "Finley", "Adam", "Dylan", "Zachary", "Riley",
    "Teddy", "Theodore", "David", "Elijah", "Reuben", "Arlo", "Hugo", "Luca", "Jaxon", "Louie",
    "Aiden", "Carter", "Wyatt", "Gabriel", "Julian", "Grayson", "Levi", "Matthew", "Jayden", "Hudson",
    "Lincoln", "Ezra", "Nathan", "Ryan", "Jace", "Caleb", "Hunter", "Christian", "Jonathan", "Eli",
    "Isaiah", "Connor", "Landon", "Adrian", "Colton", "Jordan", "Nicholas", "Dominic", "Austin", "Ian",
    "Adam", "Cooper", "Brayden", "Roman", "Miles", "Jason", "Santiago", "Sawyer", "Xavier", "Easton",
    "Parker", "Kayden", "Bentley", "Axel", "Brooks", "Micah", "Vincent", "Weston", "Silas", "Declan",
    "Evan", "Emmett", "Kingston", "Asher", "Carson", "Maverick", "Diego", "Carlos", "Ivan", "Luis",
    "Maxwell", "Kaiden", "Juan", "Bryson", "Angel", "Alex", "Greyson", "Rowan", "Harrison", "Camden",
    "Braxton", "Ryder", "Gael", "Ivan", "Jasper", "Zane", "Emmanuel", "Knox", "Beau", "Chase", "Gavin",
    "Bentley", "Jude", "Joel", "George", "Blake", "Dean", "Eric", "Finn", "Grant", "Jake", "Kaden",
    "Paxton", "Rafael", "Tucker", "Victor", "Walker", "Zion", "Abel", "Anderson", "Brody", "Caden",
    "Chance", "Clayton", "Damian", "Emerson", "Finnegan", "Holden", "Jax", "Jett", "Karter", "Kyrie",
    "Leon", "Malachi", "Nash", "Phoenix", "Reid", "Ronan", "Seth", "Spencer", "Tristan", "Wade"
]

class Command(BaseCommand):
    help = '批量重命名测试用户为英文名，并将密码同步为用户名（admin用户不修改）'

    def handle(self, *args, **options):
        test_users = CustomUser.objects.filter(username__startswith='test_user_').exclude(username='admin')
        used_names = set(CustomUser.objects.values_list('username', flat=True))
        available_names = [name for name in ENGLISH_NAMES if name not in used_names]
        random.shuffle(available_names)
        count = 0
        for user in test_users:
            if not available_names:
                self.stdout.write(self.style.ERROR('可用英文名已用尽，请扩充ENGLISH_NAMES列表'))
                break
            new_name = available_names.pop()
            user.username = new_name
            user.password = new_name  # 明文存储，和用户名一致
            user.save()
            count += 1
            self.stdout.write(self.style.SUCCESS(f'用户 {user.id} 重命名为 {new_name}，密码已同步'))
        self.stdout.write(self.style.SUCCESS(f'共处理 {count} 个测试用户'))