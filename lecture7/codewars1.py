def count_positives_sum_negatives(arr):
    '''function return sum negative number and count positive number'''
      positive_number = 0
      negative_number = 0
      for i in arr:
          if i>0:
              positive_number+=1
          elif i<0:
              negative_number+=i
          
      return [positive_number,negative_number] if arr !=[] else []