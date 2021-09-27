import { Route, Switch } from "react-router-dom";
import EmptyPage from "./component/EmptyPage";

import Estimate from "./mainPage/menu/Estimate";
import Parts from "./mainPage/menu/Parts";
import Board from "./mainPage/menu/Board";
import Share from "./mainPage/menu/Share";
import Notice from "./mainPage/menu/Notice";
import QnA from "./mainPage/menu/QnA";
import Main from "./component/Main";
import Login from "./component/Login";
import Regist from "./component/Regist";
import Header from "./component/Header";
import Footer from "./component/Footer";
import PcRecommand from "./mainPage/menu/PcEstimate/PcRecommand";

export default function Routing() {
    return (
        <Switch>
            <Route path="/Login" component={Login} />
            <Route path="/Regist" component={Regist} />
            <>
                <Header />
                <Route exact path="/" component={Main} />
                <Route path="/Estimate" component={Estimate} />
                <Route path="/Parts" component={Parts} />
                <Route path="/Board" component={Board} />
                <Route path="/Share" component={Share} />
                <Route path="/Notice" component={Notice} />
                <Route path="/QnA" component={QnA} />
                <Route path="/PcRecommand" component={PcRecommand} />
                <Footer />
            </>
        </Switch>
    );
}
