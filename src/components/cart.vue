<template>

  <div>
    <app-header>my cart</app-header>
    <div class="container-fluid pt-5 cart">
      <div class="container pt-5">
        <div class="row" v-if="products">
          <div class="col-lg-7 cart-items align-self-top mb-5">
            <div class="border p-3">
              <h4 class="p-1">My Cart [ {{products.length}} ]</h4>
              <hr>
              <div v-if="products.length < 1">
                Buy Something
                <router-link :to="{name:'Shop'}" class="text-primary">Here</router-link>
              </div>
              <div class="row my-3 border-bottom p-1" v-for="product in products" v-else>
                <div class="col-sm-5">
                  <router-link :to="'/product/'+product.slug">
                    <img :src="product.thumb" alt="product thumb">
                  </router-link>
                </div>
                <div class="col-sm-7">
                  <h5>
                    <router-link :to="'/product/'+product.slug">
                      {{product.name}}
                    </router-link>
                  </h5>
                  <span class="text-success">Rs. {{product.price}}</span>
                  <p>Size {{product.size}}</p>
                  <div class="text-right">
                    <a class="btn btn-danger btn-sm text-white" @click.prevent="cartToggle(product.id)">
                      <font-awesome-icon icon="trash-alt" class="mr-1" />Remove
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-5 total-cart" v-if="products.length > 0">
            <div class="border p-3" v-if="cart">
              <h4 class="p-1">Cart Totals</h4>
              <hr>
              <p class="d-flex p-2">
                <span>Items Count</span>
                <span>{{cart.products.length}}</span>
              </p>
              <p class="d-flex p-2">
                <span>Subtotal</span>
                <span>Rs {{cart.subtotal}}</span>
              </p>
              <p class="d-flex p-2 total border-top">
                <span>Total</span>
                <span>Rs {{cart.total}}</span>
              </p>
            </div>
            <div class="text-right">
              <router-link class="btn btn-success m-2" tag="button" :to="{name:'Checkout'}" exact>
                Checkout
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>
<script>

  import Header from './header/header.vue'

  export default {
    data() {
      return {}
    },
    components: {
      appHeader: Header
    },
    computed: {
      products() {
        return this.$store.state.cartItems.variants
      },
      cart() {
        return this.$store.state.cartItems.cart
      }
    },
    methods: {
      cartToggle(productId) {
        this.$store.dispatch('cartToggle', productId)
      }
    }
  }

</script>
<style scoped>

  a {
    color: #333;
  }

  .head {
    font-size: 1.2rem;
    padding: 1rem;
  }
  .cart img {
    max-width: 100%;
  }
  .cart input.form-control {
    max-width: 100px;
    min-width: 70px;
  }
  .total-cart span {
    display: block;
    width: 50%;
  }
  .total {
    font-size: 1.2rem;
  }
  .cart-items {
    overflow-x: auto;
  }
  .border-bottom:last-of-type {
    border-bottom: none !important;
  }

</style>
