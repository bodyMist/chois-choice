import { Route, Switch } from "react-router-dom";
import MenuList from "./component/MenuList";
import EmptyPage from "./component/EmptyPage";

import Estimate from "./menu/Estimate";
import Parts from "./menu/Parts";
import Board from "./menu/Board";
import Share from "./menu/Share";
import Notice from "./menu/Notice";
import QnA from "./menu/QnA";

export default function Routing() {
    return (
        <Switch>
            <Route exact path="/" component={MenuList} />
            <Route path="/Estimate" component={Estimate} />
            <Route path="/Parts" component={Parts} />
            <Route path="/Board" component={Board} />
            <Route path="/Share" component={Share}/>
            <Route path="/Notice" component={Notice}/>
            <Route path="/QnA" component={QnA}/>
            <Route component={EmptyPage} />
        </Switch>
    );
}
