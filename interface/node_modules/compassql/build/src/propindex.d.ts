import { Dict } from './util';
import { Property } from './property';
export interface PropIndexReader<T> {
    has(p: Property): boolean;
    get(p: Property): T;
}
/**
 * Dictionary that takes property as a key.
 */
export declare class PropIndex<T> implements PropIndexReader<T> {
    private index;
    constructor(i?: Dict<T>);
    has(p: Property): boolean;
    get(p: Property): T;
    set(p: Property, value: T): this;
    setByKey(key: string, value: T): void;
    map<U>(f: (t: T) => U): PropIndex<U>;
    size(): number;
    duplicate(): PropIndex<T>;
}
