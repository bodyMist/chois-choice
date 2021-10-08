import { BrowserRouter, Route, Switch } from "react-router-dom";
import Routing from "./Routing";

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
