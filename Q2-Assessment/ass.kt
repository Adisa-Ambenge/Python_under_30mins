fun main() {
product = Product("laptop",20000.00,5)
   println( product.calculateAverage())
    student = Student("ANgela",24,67.80)
   println( student.calculateAverage())
}
class Product(val name:String,val price:Double,val quantity:Int){
    fun calculateAverage():Double{
        var price = 2000
        var quantity = 5
        return price* quantity
    }
}

class Student(val name:String,val age:Int,val grades:Double){
    def calculateAverage():Double{
        var total = sum(grades)
        var avg = total/count(grades)
        return avg

    }
}
class FlightBooking(val destination:String,val date:String,val customer:Int,val flights:String){
    fun searchFlight(){
       var flightDestination = []
        var flightDate = []
        var availableFlight = mutableListOf<String>(){
            for (flight in flights){
                if (flightDestination == destination && flightDate){
                    return availableFlight
                }
            }
        }
    }
}
