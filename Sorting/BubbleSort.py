def Bubble_Sort(Array_Orig, Reverse = False):

	# Copy of Array so that changes made are not reflected
	Array = list(Array_Orig)

	for i in range(len(Array)):
		Max = Array[i]
		Pos = i
		for j in range(i, len(Array)):
			if not Reverse:
				if Max > Array[j]:
					Max = Array[j]
					Pos = j
			elif Reverse:
				if Max < Array[j]:
					Max = Array[j]
					Pos = j

		# Swapping the positions
		Array[i],Array[Pos] = Array[Pos],Array[i]
	return Array
