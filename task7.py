'''
7. ��������� ���������� ����������� ����������.
 � ������ ���� ��� ��������� �������� a ����������.
 ������ ���� ��������� ���������� ��������� �� 10% ������������ �����������.
 ��������� ���������� ����� ���, �� ������� ��������� ���������� �������� �� ����� b ����������.
 ��������� ������ ��������� �������� ���������� a � b � �������� ���� ����������� ����� � ����� ���.
��������: a = 2, b = 3.
���������:
1-� ����: 2
2-� ����: 2,2
3-� ����: 2,42
4-� ����: 2,66
5-� ����: 2,93
6-� ����: 3,22
�����: �� ������ ���� ��������� ������ ���������� � �� ����� 3 ��.
'''

a = int(input("���������� ���������� � ������ ���� ����������: "))
b = int(input("�������� ���������� ���������� �� ����������: "))
days = 1
print(f'{days} - �� ����: {a} ��')
while a < b:
    a = a + a * 0.1
    days += 1
    print(f'{days}-�� ����: {a} ��')
print(f'�����: �� {days} ���� ��������� ��������� ���������� - �� ����� {b} ��')
