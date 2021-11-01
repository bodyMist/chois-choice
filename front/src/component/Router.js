import { Route, Switch } from "react-router";
import Header from "./title/Header";
import Login from "./title/Login";
import Regist from "./title/Regist";
import Main from "./menu/Main";
import Estimate from "./menu/Estimate/Estimate";
import Parts from "./menu/Parts/Parts"
import Tab from "./tabs/Tab";
export default function Router() {
  return (
    <Switch>
      <Route path="/Login" component={Login} />
      <Route path="/Regist" component={Regist} />
      <>
        <Header />
        <Tab />
        <Route exact path="/" component={Main} />
        <Route path="/Estimate" component={Estimate} />
        <Route path="/Parts" component={Parts} />
      </>
    </Switch>
  );
}
