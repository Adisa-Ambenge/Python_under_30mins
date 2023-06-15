class Recipe{
    constructor(food, ingredients, preparationTime, cookingMethod, nutritionalInfo) {
        this.food = food;
        this.ingredients = ingredients;
        this.preparationTime = preparationTime;
        this.cookingMethod = cookingMethod;
        this.nutritionalInfo = nutritionalInfo;
    }

}

class Product {
    constructor(name, price, quantity) {
      this.name = name;
      this.price = price;
      this.quantity = quantity;
    }
    calculateTotal() {
      return this.price * this.quantity;
    }
  }
  let product1 = new Product("Laptop", 250000.99, 2);
  let  product2 = new Product("mouse", 500.00, 2);

  let totalValue1 = product1.calculateTotal();
  let totalValue2 = product2.calculateTotal();
  console.log(` ${product1.name}: $${totalValue1}`);
  console.log(` ${product2.name}: $${totalValue2}`);

  class Student{
    constructor(name,age,grades){
        this.name=name
        this.age=age
        this.grades=grades
    }
  }