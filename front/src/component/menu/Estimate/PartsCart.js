import list from "../menulist.json"
import { useHistory } from "react-router";
export default function SelectedParts({location}) {
  let history=useHistory();
  const goBack=()=>{
    history.push('/Estimate',[location])
  }
  return (
      <div className="container-partsCart">
        <div>
          <button onClick={goBack}>{"<"}</button>
        </div>
          <ul className="listPart">
              {list.class.map((item, index) => {
                if(location.data[index].name!="미선택") {
                  return (
                      <li className="Part-list">
                          <div className="PartName">
                              <strong>{item.name}</strong>
                          </div>
                          <div className="PartItem">
                            <div className="Part-image">
                              <img src={location.data[index].image_url}/>
                            </div>
                            <div className="Part-inf-box">
                              <span className="Part-inf">{location.data[index].name}</span>
                            </div>
                          </div>
                      </li>
                  );
                }
              })}
          </ul>
      </div>
  );
}