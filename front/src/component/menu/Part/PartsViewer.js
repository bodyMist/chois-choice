import { useState } from "react";
import PartsSelector from "./PartsSelector"
export default function Parts() {
  const [list, setList] = useState([]);
  const getPartItems = (set) => {
    //백에서 중분류 선택한것으로 정보 받아와야함.
  }

  // 옵션 선택된 것으로 정보 필터링하는거 만들어야함.
  const getItemsByOption = (checkedItems) => {
    [...checkedItems].map((items)=>{
      list.filter((list)=>list.generation == items.id)
    })
  }
  return (
    <div className="prodlist_wrap">
    <PartsSelector getPartItem={getPartItems} list={list} getItemsByOption={getItemsByOption} />
    </div>
  );
}