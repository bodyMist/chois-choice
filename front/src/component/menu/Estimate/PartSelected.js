import { style } from "@mui/system";
import { useState } from "react";
import { Link, useLocation } from "react-router-dom";
import data from "../menulist.json";
export default function PartSelected({ getPartInf, sList}) {
const location = useLocation();
  const getPartName = (e) => {
    const id = e.target.id;
    let select = [
      {"selected":0}, {"selected":0}, {"selected":0}, {"selected":0}, 
      {"selected":0}, {"selected":0}, {"selected":0}, {"selected":0}, 
      {"selected":0}
  ]
    select[id-1].selected=1
    setSelected(select)
    getPartInf(id);
  };
  const[selected, setSelected] = useState([
    {"selected":1}, {"selected":0}, {"selected":0}, {"selected":0}, 
    {"selected":0}, {"selected":0}, {"selected":0}, {"selected":0}, 
    {"selected":0}
]);

  return (
    <>
    <div className="MainSufferArear">
      {data.class.map((classData) => (
        <div className="WillSelect StuffOnePart">
          <div
            className="text StuffInfor"
            id={classData.id}
            onClick={getPartName}
          >
            {classData.name} : {sList[classData.id - 1].name}
          </div>
        </div>
      ))}
    </div>
    <div className="MobileSufferArear">
    <div className="ShowSelectedParts" >
     <Link to={{
       pathname:"/PartsCart",
       data: sList,
     }}>선택부품</Link>
    </div>
    {data.class.map((classData) => (
        <div className="WillSelect StuffOnePart">
          <div
            className= {(selected[classData.id-1].selected == 1 ? "Selected" : '')+" text StuffInfor"}
            id={classData.id}
            onClick={getPartName}
          >
            {classData.name}
            <span 
            className={(sList[classData.id-1].name != "미선택" ? "checked" : 'notChecked')}
            id={classData.id}
            >&nbsp;✔&nbsp;</span>
          </div>
        </div>
      ))}
      
    </div>
    
    </>
  );
}
