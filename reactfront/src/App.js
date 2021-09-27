import Header from "./component/Header";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Footer from "./component/Footer";
import Routing from "./Routing";
import Main from "./component/Main";
import Estimate from "./mainPage/menu/Estimate";
import Parts from "./mainPage/menu/Parts";
import Board from "./mainPage/menu/Board";
import Share from "./mainPage/menu/Share";
import Notice from "./mainPage/menu/Notice";
import QnA from "./mainPage/menu/QnA";
import Login from "./component/Login";
import Regist from "./component/Regist";
import EmptyPage from "./component/EmptyPage";

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Switch>
                    <Routing/>
                </Switch>
            </div>
        </BrowserRouter>
    );
}

export default App;
