import { useState, useEffect } from "react"
import styled from "styled-components"
import { transactions as data } from "./data"

const List = styled.table`
    text-align: center;
    border: 5px solid grey;
    border-spacing: 0;
    th {
        background-color: blue;
        color: white;
        font-weight: bold;
        padding: 0.5rem 0;
    }
    td {
        border-top: 1px solid blue;
        border-right: 1px solid blue;
        padding: 0.5rem 0;

        &:last-child {
            border-right: 0;
        }
    }
    width: 100%;
`

export default function TransactionList() {
    const [transactions, setTransactions] = useState([])

    useEffect(() => {
        const ts = data.map((t) => {
            const date = new Date(t.datetime)
            const formatted_date = `${date.getDate()}/${date.getMonth()}/${date.getFullYear()}`
            return { ...t, datetime: formatted_date }
        })
        setTransactions(ts)
    }, [])

    return (
        <List>
            <tr>
                <th>Date</th>
                <th>Name</th>
                <th>Amount</th>
                <th>Bucket</th>
                <th>Category</th>
                <th>Is Real?</th>
            </tr>
            {transactions.map((transaction) => {
                return (
                    <tr key={transaction.id}>
                        <td>{transaction.datetime}</td>
                        <td>{transaction.name}</td>
                        <td>{transaction.amount}</td>
                        <td>{transaction.bucket}</td>
                        <td>{transaction.category}</td>
                        <td>{transaction.is_real ? "Real" : "Estimated"}</td>
                    </tr>
                )
            })}
        </List>
    )
}
