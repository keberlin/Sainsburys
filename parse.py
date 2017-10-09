import glob, csv, re

MON = 0
TUE = 1
WED = 2
THU = 3
FRI = 4
DAYS = ['mon','tue','wed','thu','fri']
DESCRIPTION = 'description'
SQUARE = 'square'
DOUBLE = 'double'

def find_day(day,l):
    try:
        i = l.index(day)
        return i
    except:
        pass
    d = DAYS.index(day)
    for i, item in enumerate(l):
        m = re.match('(?P<a>[a-z]{3})-(?P<b>[a-z]{3})',item)
        if m:
            if DAYS.index(m.group('a')) <= d <= DAYS.index(m.group('b')):
                return i
    print "Error: Could not find day %s in %s" % (day,l)

for filename in glob.glob('*.csv'):
    with open(filename, 'rb') as csvfile:                                                                                                
        reader = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(reader):
            if i == 0:
                # handle the header
                header = row
            elif i == 1:
                # handle the data
                data = row

        results = []
        for day in DAYS:
            d = DAYS.index(day)
            if MON <= d <= WED:
                type = SQUARE
            else:
                type = DOUBLE
            # find the day column within the header
            i = find_day(day,header)
            value = int(data[i])
            if type == SQUARE:
                value = value*value
            elif type == DOUBLE:
                value = value*2
            # find the description column in the header
            i = header.index(DESCRIPTION)
            description = data[i] + ' ' + str(value)
            result = {
                'day': day,
                'description': description,
                type: value,
                'value': value,
            }
            results.append(result)
        print filename
        print results
