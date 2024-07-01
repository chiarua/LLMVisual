import { Channel } from 'vega-lite/build/src/channel';
import { FacetedUnitSpec } from 'vega-lite/build/src/spec';
import { PropIndex } from '../propindex';
import { Dict } from '../util';
import { SHORT_WILDCARD } from '../wildcard';
import { EncodingQuery, FieldQueryBase } from './encoding';
import { SpecQuery } from './spec';
export declare type Replacer = (s: string) => string;
export declare function getReplacerIndex(replaceIndex: PropIndex<Dict<string>>): PropIndex<Replacer>;
export declare function getReplacer(replace: Dict<string>): Replacer;
export declare function value(v: any, replacer: Replacer): any;
export declare function replace(v: any, replacer: Replacer): any;
export declare const REPLACE_NONE: PropIndex<Replacer>;
export declare const INCLUDE_ALL: PropIndex<boolean>;
export declare function vlSpec(vlspec: FacetedUnitSpec, include?: PropIndex<boolean>, replace?: PropIndex<Replacer>): string;
export declare const PROPERTY_SUPPORTED_CHANNELS: {
    axis: {
        x: boolean;
        y: boolean;
        row: boolean;
        column: boolean;
    };
    legend: {
        color: boolean;
        opacity: boolean;
        size: boolean;
        shape: boolean;
    };
    scale: {
        x: boolean;
        y: boolean;
        color: boolean;
        opacity: boolean;
        row: boolean;
        column: boolean;
        size: boolean;
        shape: boolean;
    };
    sort: {
        x: boolean;
        y: boolean;
        path: boolean;
        order: boolean;
    };
    stack: {
        x: boolean;
        y: boolean;
    };
};
/**
 * Returns a shorthand for a spec query
 * @param specQ a spec query
 * @param include Dict Set listing property types (key) to be included in the shorthand
 * @param replace Dictionary of replace function for values of a particular property type (key)
 */
export declare function spec(specQ: SpecQuery, include?: PropIndex<boolean>, replace?: PropIndex<Replacer>): string;
/**
 * Returns a shorthand for an encoding query
 * @param encQ an encoding query
 * @param include Dict Set listing property types (key) to be included in the shorthand
 * @param replace Dictionary of replace function for values of a particular property type (key)
 */
export declare function encoding(encQ: EncodingQuery, include?: PropIndex<boolean>, replace?: PropIndex<Replacer>): string;
/**
 * Returns a field definition shorthand for an encoding query
 * @param encQ an encoding query
 * @param include Dict Set listing property types (key) to be included in the shorthand
 * @param replace Dictionary of replace function for values of a particular property type (key)
 */
export declare function fieldDef(encQ: EncodingQuery, include?: PropIndex<boolean>, replacer?: PropIndex<Replacer>): string;
export declare function parse(shorthand: string): SpecQuery;
/**
 * Split a string n times into substrings with the specified delimiter and return them as an array.
 * @param str The string to be split
 * @param delim The delimiter string used to separate the string
 * @param number The value used to determine how many times the string is split
 */
export declare function splitWithTail(str: string, delim: string, count: number): string[];
export declare namespace shorthandParser {
    function encoding(channel: Channel | SHORT_WILDCARD, fieldDefShorthand: string): EncodingQuery;
    function rawFieldDef(fieldDefPart: string[]): FieldQueryBase;
    function getClosingIndex(openingBraceIndex: number, str: string, closingChar: string): number;
    function fn(fieldDefShorthand: string): FieldQueryBase;
}
