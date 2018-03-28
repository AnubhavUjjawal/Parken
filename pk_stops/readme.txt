Templates needed to be created
	pk_spots
		book_spot.html
			context
				open_spots
					type: List
					model: Spot
				previous_bookings
					type: List
					model: Booking
			other requirements
				create a form with inputs of Booking, field in html should be foriegn key spot=>open_spots.id, booked_by=>request.user		
				
	auth
		login.html
			requirements: username, password, err msg.