import { BrowserRouter, Switch } from "react-router-dom";
import Main from "./component/menu/Main";
import Router from "./component/Router"
function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Switch>
          <Router />
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;
