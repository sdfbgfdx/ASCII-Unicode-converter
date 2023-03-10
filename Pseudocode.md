Request user input

Function choose_mode():
	If user responds "ASCII":
		Set conversion to ASCII
		Request string
	Else if user responds "Unicode":
		Set conversion to "Unicode"
		Request string

Function apply_conversion():
	If conversion is "ASCII":
		Split string into characters
		If character is not a valid ASCII character:
			Return error message
		Else:
			Convert character to Unicode
		Combine Unicode characters into answer
		Display answer
	Else If conversion is "Unicode":
		Split string into integers
		If integer has no corresponding ASCII characters:
			Return error message
		Else:
			Convert integer into ASCII
		Combine ASCII characters into answer
		Display answer
