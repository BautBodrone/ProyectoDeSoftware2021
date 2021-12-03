
<template>
  <div class="max-w-xl mx-auto px-4">
    <div class="rounded-lg shadow-lg p-4">
    <Form>

      <form>

  <p>
    <label for="titulo">Titulo</label>
    <input
      id="titulo"
      v-model="titulo"
      type="text"
      name="titulo"
      maxlength="30"
    >
  </p>
  <p>
    <label for="apellido_denunciante">Apellido</label>
    <input
      id="apellido_denunciante"
      v-model="apellido_denunciante"
      type="text"
      name="apellido_denunciante"
      maxlength="30"
    >
  </p>
  <p>
    <label for="nombre_denunciante">nombre_denunciante</label>
    <input
      id="nombre_denunciante"
      v-model="nombre_denunciante"
      type="text"
      name="nombre_denunciante"
      maxlength="30"
    >
  </p>
  <p>
    <label for="email_denunciante">Email</label>
    <input
      id="email_denunciante"
      v-model="email_denunciante"
      type="text"
      name="email_denunciante"
      maxlength="30"
    >
  </p>
 
  <p>
    <label for="telcel_denunciante">Telefono</label>
    <input
      id="telcel_denunciante"
      v-model="telcel_denunciante"
      type="number"
      name="telcel_denunciante"
      min="100000">
  </p>
 <p>
    <label for="descripcion">Descripcion</label>
    <textarea
      id="descripcion"
      v-model="descripcion"
      type="text"
      name="descripcion"
    ></textarea>
  </p>
  <p>
    <label for="movie">Película favorita</label>
    <select
      id="movie"
      v-model="movie"
      name="movie"
    >
      <option>Star Wars</option>
      <option>Vanilla Sky</option>
      <option>Atomic Blonde</option>
    </select>
  </p>

  <p>
    <input
      type="submit"
      value="Enviar"
    >
  </p>

</form>
</Form>
    </div>
  </div>


      <!--
    <div
      v-for="{ as, name, label, children, ...attrs } in schema.fields"
      :key="name"
    >
      <label :for="name">{{ label }}</label>
      <Field :as="as" :id="name" :name="name" v-bind="attrs">
        <template v-if="children && children.length">
          <component v-for="({ tag, text, ...childAttrs }, idx) in children"
            :key="idx"
            :is="tag"
            v-bind="childAttrs"
          >
            {{ text }}
          </component>
        </template>
      </Field>
      <ErrorMessage :name="name" />
    </div>
    <button>Submit</button>
    -->
  
</template>
<script>
import { Form,// Field, ErrorMessage 
} from 'vee-validate';
export default {
  name: 'DynamicForm',
  components: {
    Form,
    //Field,
    //ErrorMessage
  },
  props: {
    schema: {
      type: Object,
      required: true,
    },
  },
};
</script>
