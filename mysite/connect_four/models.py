from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    '''
    User1 will use x
    User2 will use o
    '''
    row1 = models.CharField(max_length=7, default="-------")
    row2 = models.CharField(max_length=7, default="-------")
    row3 = models.CharField(max_length=7, default="-------")
    row4 = models.CharField(max_length=7, default="-------")
    row5 = models.CharField(max_length=7, default="-------")
    row6 = models.CharField(max_length=7, default="-------")
    user1 = models.ForeignKey(User, related_name='user1')
    user2 = models.ForeignKey(User, related_name='user2')
    next_turn = models.ForeignKey(User, related_name='user_next_turn')

    def get_rows(self):
        rows = []
        for row in self.row1, self.row2, self.row3, self.row4, self.row5, self.row6:
            r = list(row)
            rows.append(r)
        return rows

    def user_won(self):
        won = False
        return won

    def move(self, user, column):
        moved = False
        if user == self.user1:
            mark = "x"
            next_t = self.user2
        else:
            mark = "o"
            next_t = self.user1

        if user == self.next_turn:
            for row_index in range(1,6):
                field_name = "row{}".format(row_index)
                row = getattr(self, field_name)
                if row[column] == "-":
                    row = row[:column] + mark + row[column+1:]
                    setattr(self, field_name, row)
                    moved = True
                    self.next_turn = next_t
                    self.save(update_fields=["row{}".format(row_index), "next_turn"])
                    print(row_index)
                    break
        if moved == False:
            # no row free for this column or the user didn't have the turn
            return None
        else:
            return self.get_rows()

    def __str__(self):
        return "Board of {} with {}".format(self.user1, self.user2)
