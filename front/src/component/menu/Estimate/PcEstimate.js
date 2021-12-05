import { Link } from "react-router-dom";
import PartSelect from "./PartSelect";
import PartSelected from "./PartSelected";
import axios from "axios";
import { useState } from "react";
import { useEffect } from "react";

export default function PcEstimate() {
  const [list, setList] = useState([]);
  const [fList, setFList] = useState([]);
  const [page, setPage] = useState(1);
  const [sList, setSlist] = useState([
    { id: 1, name: "미선택" },
    { id: 2, name: "미선택" },
    { id: 3, name: "미선택" },
    { id: 4, name: "미선택" },
    { id: 5, name: "미선택" },
    { id: 6, name: "미선택" },
    { id: 7, name: "미선택" },
    { id: 8, name: "미선택" },
    { id: 9, name: "미선택" },
  ]);
  useEffect(() => {
    axios
      .get(`/component?id=1`)
      .then((response) => {
        setFList(response.data);
        setListByPage([...response.data]);
        console.log(response.data)
      })
      .catch((e) => {
        console.error(e);
      });
  }, []);


  const pageHandler = (pg) => {
    console.log(pg)
    setPage(pg);
    let array = [];
    let start = (pg - 1) * 10;
    for (let i = start; i < start + 10; i++) {
      if(fList[i])
      array = [...array, fList[i]];
    }
    setList([...array]);
  };

  const setListByPage = (li) => {
    let array = [];
    let start = (page - 1) * 10;
    for (let i = start; i < start + 10; i++) {
        if(li[i])
            array = [...array, li[i]];
    }
    setList([...array]);
};

  const getPartInf = (id) => {
    axios
      .get(`/component`, { params: { id } })
      .then((response) => {
        setFList(response.data);
        setListByPage(response.data)
      })
      .catch((e) => {
        console.error(e);
      });
  };

  const selectPart = (component_id) => {
    const l = list.filter((list) => list.component_id == component_id)[0];
    let array = [...sList];
    array[l.data_type - 1] = { id: l.data_type, name: l.name };
    setSlist(array);
  };

  const resetPart = () => {
    const id = list[0].data_type;
    axios
      .get(`/component`, { params: { id } })
      .then((response) => {
        setFList(response.data);
      })
      .catch((e) => {
        console.error(e);
      });
  }

  const searchPart = () => {
    const word = document.querySelector(".form-control").value;
    const data_type = list[0].data_type;
    axios
      .get(`/component`, {
        params: {
          id: data_type,
          word,
        },
      })
      .then((response) => {
        console.log(response.data)
        if(response.data.length === 0) {
          alert("검색 결과가 없습니다.")
        }
        else {
          setFList(response.data)
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  const onKeyPress = (e) => {
    if(e.key==='Enter') {
      searchPart()
    }
  }
  const none = {
    display: "none",
  }
  return (
      <div className="container">
          {/* <h3>PC 견적</h3> */}
          <Link to="/PcRecommand">견적 추천</Link>
          <div className="container-pc">
              <div className="searchInputArea">
                  <form className="input-group" onKeyPress={onKeyPress}>
                      <input
                          type="text"
                          className="form-control"
                          placeholder="부품 명 검색"
                      ></input>
                      <input type="text" style={none} />
                      <div className="input-group-btn">
                          <button
                              className="btn btn-default"
                              type="button"
                              onClick={searchPart}
                              id="search"
                          >
                              검색
                          </button>
                          <button
                              className="btn btn-default"
                              type="reset"
                              onClick={resetPart}
                          >
                              초기화
                          </button>
                      </div>
                  </form>
              </div>
              <PartSelect
                  list={list}
                  selectPart={selectPart}
                  page={page}
                  pageHandler={pageHandler}
                  count={fList.length}
              />
              <PartSelected getPartInf={getPartInf} sList={sList} />
              
          </div>
          
      </div>
  );
}
