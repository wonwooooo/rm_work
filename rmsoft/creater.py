class AutoIncrement:

    def __init__(self, last_col, last_field, keyword):
        self.last_col = last_col
        self.last_field = last_field
        self.keyword = keyword

    def four_padding(self):
        last_model = self.model.objects.all().order_by(self.field_name).last()
        if not last_model:
            return self.keyword  + '0000'
        # getattr를 사용해서 String상태의 field_name으로 필드 값을 가져왔다
        last_field = getattr(last_model, self.field_name)
        last_field_int = int(last_field[0:])
        new_field_val = last_field_int + 1
        new_field_val = self.keyword + str(new_field_val).zfill(4)
        return new_field_val

    if __name__ == '__main__':
        four_padding()
