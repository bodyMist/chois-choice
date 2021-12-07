import axios from "axios";
import { useEffect, useState } from "react";
import PartsSelector from "./PartsSelector";
import ItemList from "./ItemList";
import Paging from "../../Paging";
export default function PartsViewer() {
    
    const [page, setPage] = useState(1);
    const [list, setList] = useState([]);
    const [fList, setFList] = useState([]);
    const [filter, setFilter] = useState([]);
    const [isFilter, setIsFilter] = useState(false);
    useEffect(() => {
        axios
            .get(`/component/cpu/list`)
            .then((response) => {
                setFList([...response.data.reverse()]);
                setListByPage([...response.data])
            })
            .catch((e) => {
                console.error(e);
            });
    }, []);
    const getItemsByOption = (checkedItems) => {
        if (checkedItems.size != 0) {
            let array = [];
            [...checkedItems].map((items) => {
                const newList = fList.filter((listItem) => {
                    return JSON.stringify(listItem).indexOf(items) != -1;
                });
                array = [...array, ...newList];
            });
            setIsFilter(true)
            setFilter([...array]);
            let farray = [];
            let start = (page - 1) * 10;
            for (let i = start; i < start + 10; i++) {
                    if(array[i]) {
                        console.log(1)
                        farray = [...farray, array[i]];
                    }
                        
            }
            setList([...farray]);
        } else {
            setIsFilter(false);
            let array = [];
            let start = (page - 1) * 10;
            for (let i = start; i < start + 10; i++) {

                array = [...array, fList[i]];
            }
            setList([...array]);
        }
    };
    const pageHandler = (pg) => {
        setPage(pg);
        let array = [];
        let start = (pg - 1) * 10;
        for (let i = start; i < start + 10; i++) {
            if(isFilter) 
            {
                if(filter[i]) {
                    array = [...array, filter[i]];
                }
            }
            else {
                if(fList[i]) {
                    array = [...array, fList[i]];
                }
            }
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
    const getPartItems = (id) => {
        //중분류 선택한것으로 백에서 정보 받아와야함.
        axios
            .get(`/component/${id}/list`)
            .then((response) => {
                setFList(response.data.reverse());
                setListByPage([...response.data])
                console.log(response.data)
            })
            .catch((e) => {
                console.error(e);
            });
    };
   
    return (
        <div className="prodlist_wrap">
            <PartsSelector
                getPartItems={getPartItems}
                getItemsByOption={getItemsByOption}
            />
            <ItemList list={list} />
            <Paging page={page} count={isFilter ? filter.length : fList.length} pageHandler={pageHandler}/>
        </div>
    );
}
