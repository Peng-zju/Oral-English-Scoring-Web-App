import Vue from 'vue'
import { Button,ButtonGroup, Form, FormItem, Input, Row, Message, Container, Header, Menu, MenuItem, Table, TableColumn, Tag, Card, Col, Select, Dialog, Option, MessageBox, Divider} from 'element-ui'

Vue.use(Button);
Vue.use(ButtonGroup);
Vue.use(Form);
Vue.use(FormItem);
Vue.use(Input);
Vue.use(Row);
Vue.use(Container);
Vue.use(Header);
Vue.use(Menu);
Vue.use(MenuItem);
Vue.use(Table);
Vue.use(TableColumn);
Vue.use(Tag);
Vue.use(Card);
Vue.use(Col);
Vue.use(Select);
Vue.use(Dialog);
Vue.use(Option);
Vue.use(Divider)
Vue.prototype.$message = Message;
Vue.prototype.$confirm = MessageBox.confirm;

