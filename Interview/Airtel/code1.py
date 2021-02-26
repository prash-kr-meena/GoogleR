"""
Airtel is also in a growing phase, they are right now focused in developing
code-quality is decent and they are planning to have good code-coverage around 70-75 % is there expectation
They have sonar-qube instances which they use to monitor
The guy was not sure about if they had something like new-relic with them to monitor there requests

they work on spring-boot, they also do not have any DB
Team is called ESB -> Enterprise Service Bus
They use Apaches Camel and Kafka

They are kind of in the middle of the layer --> there are some services that call them, and they call some of there downstream

Based out of Gurgaon


I have asked in the range of 23-25 from them

-------------------------------------------------------------------------------------------

* asked difference bw inheritance and composition,
    and why do you need them
    where would you apply them?

    i explained composition is used in kind of dependency injection?
    Not 100% sure but yeah


* Difference bw and abstract class and Interfaces
    Where would you use them and for what reasons?

* asked me to implement my own class and
    implement its equals and hashcode methods
    - Proof your, implementation works
    - by creating two ojbects and checking there equality

"""

"""
# --------------- Java Code I Wrote ---------------

package com.company;

public class Animal {

  private String name;
  private Integer age;

  public Animal(String name, Integer age) {
    this.name = name;
    this.age = age;
  }

  // equals and hashcode

  @Override
  public boolean equals(Object obj) {
    if (obj == null) {
      return false;
    }

    if (!(obj instanceof Animal)) {
      return false;
    }

    Animal animal = (Animal) obj;
    return animal.name.equals(this.name) && animal.age.equals(this.age);
  }

  @Override
  public int hashCode() {
    int hash = 1;
    int prime = 31;
    char[] chars = this.name.toCharArray();

    int upperPower = age;
    int power = 1;
    for (char ch : chars) {
      hash += ch * Math.pow(prime, power);
      if (power == upperPower) {
        power = 1;
      }
      power++;
    }

    return hash;
  }

  @Override
  public String toString() {
    return "Animal{" +
        "name='" + name + '\'' +
        ", age=" + age +
        '}';
  }

  public static void main(String[] args) {
    Animal animal_1 = new Animal("dog", 2);
    Animal animal_2 = new Animal("dog", 2);

    System.out.println(animal_1.equals(animal_2));
    System.out.println(animal_1 + " -- " + animal_2);

    animal_2.age = 3;
    System.out.println(animal_2);
    System.out.println(animal_1);
  }
}
"""
