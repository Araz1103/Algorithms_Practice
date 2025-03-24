def generate(numRows: int)

        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1], [1, 1]]

        output_rows = [[1], [1,1]]

        for i in range(3, numRows+1):
            last_row = output_rows[-1]
            # To make new row
            # We know first and last element is 1 and 1
            # All others are through sum of prev row pairs
            new_row = [1] #Starts with 1
            for num in range(len(last_row)-1):
                new_row.append(last_row[num] + last_row[num+1])
            new_row.append(1) #Ends with 1
            output_rows.append(new_row)
        
        return output_rows