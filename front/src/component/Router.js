import { Route, Switch } from "react-router";
import Header from "./title/Header";
import Login from "./title/Login";
import Regist from "./title/Regist";
import Main from "./menu/Main";
import Estimate from "./menu/Estimate/Estimate";
import PartsViewer from "./menu/Part/PartsViewer"
import Tab from "./tabs/Tab";
import PcRecommand from "./menu/Estimate/PcRecommand";
import Board from "./menu/Board/Board";
import ComponentDetail from "./menu/Part/ComponentDetail";
import PartsCart from "./menu/Estimate/PartsCart";
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
        <Route path="/Parts" component={PartsViewer} />
        <Route path="/PcRecommand" component={PcRecommand} />
        <Route path="/Board" component={Board} />
        <Route path="/ComponentDetail" component={ComponentDetail} />
        <Route path="/PartsCart" component={PartsCart} />
      </>
    </Switch>
  );
}
