"""
// Booking id is Unique
public static String generateBookingNum(long bookingId) {
   //assuming booking id length will not exceed 10
   final int crnLength = 11;
   int bookingIdLength = (int) (Math.log10(bookingId) + 1);
   int randLength = crnLength - bookingIdLength;

   _-_-_-_-234
   34 234 234
   abcdefg234


   StringBuilder crn = new StringBuilder();
   for (int i=0 ; i < randLength; i++) {
       crn.append("1");
   }
   crn.append(bookingId+””);
   return crn.toString();
}




bookingIdLength  = 123   234


log(123) = 2.8
bookingIdLength = 3

11 - 3

randLength 8

11 - len(bookingId)
              0 1 2 3 3 4  . . . 11 … INT_Max

randLength  11, 10 , 9, 8 , 7  6  . .  0 . . - INT_MAX
randLength  11, 10 , 9, 8 , 7  6  . .  1        AFter our assumption


11111111234
11111111234

1234
234

==============================================================================



Rating System

After the end of a typical ride at Oye! Rickshaw the passenger is presented with the option to rate a ride.

As a part of this exercise we would like you to design and implement the backend of a rating service.

The solution should support

The passenger should be able to rate a given ride.
The driver should be able to see aggregated rating of his all rides
The driver should be able to rate the passenger after ride
The passenger should be able to see his aggregated rating based on all the rides he has taken.

You can use any language or framework for this problem. You may reach out to us in case you need any clarification or have any questions.

Consumer App
/rate
{
  booking_id
  User_id
  Stars_To_Driver  → to Driver
  Comment
}

Driver App
/rate
{
  booking_id
  driver_id
  Stars_To_Customer     → to user
  Comment
}


StartTable
      User_id
      driver_id
	booking_Id
      Stars_To_Driver   = NUll Possible
      Stars_To_Customer = NUll Possible


User Table
	User_id

Driver Table
	Driver_id






Query to get the aggregate (avg) rating for the CUstomer for all of its rides
Select avg(Stars_To_Customer) form star_table where user_id = XYZ


Query to get the aggregate (avg) rating for the Driver for all of its rides
Select avg(Stars_To_Driver) form star_table where driver_id = XYZ

"""
