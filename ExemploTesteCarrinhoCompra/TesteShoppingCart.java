/**
* Engenharia de Software Moderna - Testes  (Cap. 8)
* Prof. Marco Tulio Valente
* 
* Exercício simples de teste de unidade (ShoppingCart)
*
*/

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;
import java.util.ArrayList;
import java.util.List;

public class TesteShoppingCart {

  private ShoppingCart shoppingCart;

  @Before
  public void setUp() {
    shoppingCart = new ShoppingCart();
    shoppingCart.addItem(new Item("ESM", 65.0));
    shoppingCart.addItem(new Item("GoF", 120.0));
  }

  @Test
  public void testAddItem() {
    Item newItem = new Item("Clean Code", 100.0);
        shoppingCart.addItem(newItem);
        assertTrue(shoppingCart.getItems().contains(newItem));
        assertEquals(3, shoppingCart.getItemCount());
  }

  @Test
  public void testRemoveItem() {
    Item itemToRemove = shoppingCart.getItems().get(0); 
        shoppingCart.removeItem(itemToRemove);
        assertFalse(shoppingCart.getItems().contains(itemToRemove));
        assertEquals(1, shoppingCart.getItemCount());
  }

  @Test
  public void testGetTotalPrice() {
    double totalPrice = shoppingCart.getTotalPrice();
    assertEquals(185.0, totalPrice, 0.01);
  }

  @Test
  public void testClearCart() {
    shoppingCart.clearCart();
    assertTrue(shoppingCart.getItems().isEmpty());
    assertEquals(0, shoppingCart.getItemCount());
  }
}
