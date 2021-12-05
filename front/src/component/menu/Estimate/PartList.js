import { useEffect } from "react";
import Part from "./Part";

export default function PartList({list, selectPart}) {
  console.log(list);
  return (
    <tbody className="StuffList">
      {list.map((listdata) => (
        <Part 
        list={listdata}
         selectPart={selectPart}
         key={listdata.component_id}
        />
      ))}
    </tbody>
  );
}